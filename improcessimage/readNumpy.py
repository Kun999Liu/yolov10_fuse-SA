import numpy as np
from ultralytics.data.utils import readTif
from pathlib import Path
import glob
import os

# 假设我们有一个名为 'data.npy' 的文件
filename = r"G:\wanxingyu\project\yolov10\yolov10-fuse\datasets\mydata\images\test\GF2_PMS1_E82.7_N45.2_20220430_L1A0006441524-pansharpen2colNum_28rowNum_48.npy"
# filename2 = r"E:\pycharmProjects\fusey10\yolov10\datasets\mydata\images\val\GF2_PMS1_E106.4_N37.4_20220326_L1A0006370789-pansharpencolNum_42rowNum_43.tif"

current_folder = 'datasets/mydata/images/test'
another_folder = 'datasets/mydata/images2/test'

# tif_files = glob.glob(os.path.join(current_folder, '*.tif'))
# npy_files = glob.glob(os.path.join(current_folder, '*.npy'))


# for tif_file in npy_files:
#     data = np.load(Path(tif_file))
#     print(data.shape)

# f = Path(filename)


# im_width, im_height, im_bands, projection, geotrans, im = readTif(filename2)
# print("tif影像：", im, "tif大小：",im.shape)

# np.save(f.as_posix(), im, allow_pickle=False)
# 现在 data 变量中包含了 .npy 文件中的数组

# 使用 numpy.load 函数读取文件
data = np.load(filename)

# 我们可以打印它的形状以确认读取成功
print(data.shape)

# 如果需要，也可以打印数组的内容
# print('numpy值：', data)
