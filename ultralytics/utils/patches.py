# Ultralytics YOLO 🚀, AGPL-3.0 license
"""Monkey patches to update/extend functionality of existing functions."""

import time
from pathlib import Path

import cv2
import numpy as np
import torch

# OpenCV Multilanguage-friendly functions ------------------------------------------------------------------------------
_imshow = cv2.imshow  # copy to avoid recursion errors


def imread(filename: str, flags: int = cv2.IMREAD_COLOR):
    """
    Read an image from a file.

    Args:
        filename (str): Path to the file to read.
        flags (int, optional): Flag that can take values of cv2.IMREAD_*. Defaults to cv2.IMREAD_COLOR.

    Returns:
        (np.ndarray): The read image.
    """
    return cv2.imdecode(np.fromfile(filename, np.uint8), flags)


def imwrite(filename: str, img: np.ndarray, params=None):
    """
    Write an image to a file.

    Args:
        filename (str): Path to the file to write.
        img (np.ndarray): Image to write.
        params (list of ints, optional): Additional parameters. See OpenCV documentation.

    Returns:
        (bool): True if the file was written, False otherwise.
    """
    # try:
    #     cv2.imencode(Path(filename).suffix, img, params)[1].tofile(filename)
    #     return True
    # except Exception:
    #     return False
    try:
        filename = Path(filename)

        # 如果后缀是 .npy，改成 .jpg 保存
        if filename.suffix.lower() == ".npy":
            filename = filename.with_suffix(".jpg")

        # 如果是 float，归一化到 0-255
        if np.issubdtype(img.dtype, np.floating):
            img = (img * 255).clip(0, 255).astype(np.uint8)

        # 如果是单通道，转换成3通道
        if img.ndim == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        elif img.ndim == 3 and img.shape[2] == 1:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        # 创建父目录
        filename.parent.mkdir(parents=True, exist_ok=True)

        # 保存图片
        success, encoded = cv2.imencode(filename.suffix, img, params or [])
        if not success:
            print(f"[ERROR] imencode failed for {filename}")
            return False

        encoded.tofile(str(filename))
        print(f"[OK] Saved image to {filename}")
        return True

    except Exception as e:
        print(f"[EXCEPTION] Failed to save {filename}: {e}")
        return False


def imshow(winname: str, mat: np.ndarray):
    """
    Displays an image in the specified window.

    Args:
        winname (str): Name of the window.
        mat (np.ndarray): Image to be shown.
    """
    _imshow(winname.encode("unicode_escape").decode(), mat)


# PyTorch functions ----------------------------------------------------------------------------------------------------
_torch_save = torch.save  # copy to avoid recursion errors


def torch_save(*args, use_dill=True, **kwargs):
    """
    Optionally use dill to serialize lambda functions where pickle does not, adding robustness with 3 retries and
    exponential standoff in case of save failure.

    Args:
        *args (tuple): Positional arguments to pass to torch.save.
        use_dill (bool): Whether to try using dill for serialization if available. Defaults to True.
        **kwargs (any): Keyword arguments to pass to torch.save.
    """
    try:
        assert use_dill
        import dill as pickle
    except (AssertionError, ImportError):
        import pickle

    if "pickle_module" not in kwargs:
        kwargs["pickle_module"] = pickle

    for i in range(4):  # 3 retries
        try:
            return _torch_save(*args, **kwargs)
        except RuntimeError as e:  # unable to save, possibly waiting for device to flush or antivirus scan
            if i == 3:
                raise e
            time.sleep((2**i) / 2)  # exponential standoff: 0.5s, 1.0s, 2.0s
