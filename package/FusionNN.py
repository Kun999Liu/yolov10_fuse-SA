# -*- coding: utf-8 -*-
# @Time    : 2025/11/5 20:43
# @Author  : Liu Kun
# @Email   : liukunjsj@163.com
# @File    : FusionNN.py
# @Software: PyCharm

"""
Describe:
"""
import os
import traceback
import xml.etree.ElementTree as ET
import ultralytics.models.yolov10.model as YOLOv10
# 避免 MKL 报错
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

def read_config(xml_path="config.xml"):
    """读取XML配置文件并支持相对/绝对路径"""
    try:
        print("正在加载配置文件:", xml_path)
        tree = ET.parse(xml_path)
        root = tree.getroot()

        device = root.findtext("device", default="0")
        input_folder = root.findtext("input_folder", default="./testimages")
        output_folder = root.findtext("output_folder", default="./runs/detect/pre")

        # 将路径转换为绝对路径（相对于exe所在目录）
        base_dir = os.path.dirname(os.path.abspath(__file__))
        input_folder = os.path.abspath(os.path.join(base_dir, input_folder))
        output_folder = os.path.abspath(os.path.join(base_dir, output_folder))

        print(f"device: {device}")
        print(f"输入路径: {input_folder}")
        print(f"输出路径: {output_folder}")

        return device, input_folder, output_folder
    except Exception as e:
        print(f"配置文件读取失败: {e}")
        input("按回车键退出...")
        exit(1)


def ensure_dir_exists(path):
    """自动创建不存在的文件夹"""
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        print(f"已创建输出目录: {path}")


def run_detection():
    """主函数"""
    # === 读取配置 ===
    device, input_folder, output_folder = read_config()

    # === 检查输入路径 ===
    if not os.path.exists(input_folder):
        print(f"输入文件夹不存在: {input_folder}")
        input("按回车键退出...")
        exit(1)

    # === 自动创建输出文件夹 ===
    ensure_dir_exists(output_folder)

    # === 定位模型权重路径 ===
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "weights", "best.pt")

    if not os.path.exists(model_path):
        print(f"权重文件未找到: {model_path}")
        input("按回车键退出...")
        exit(1)

    # === 加载模型 ===
    print("📦 正在加载模型，请稍候...")
    model = YOLOv10(model_path)

    # === 开始预测 ===
    print("模型加载完成，开始预测...")
    model.predict(
        source=input_folder,
        imgsz=416,
        cache='disk',
        workers=0,
        device=device,
        exist_ok=True,
        save=True,
        visualize=False,
        name=output_folder
    )

    print(f"✅ 预测完成！结果已保存至: {output_folder}")
    input("按回车键退出程序...")


if __name__ == '__main__':
        run_detection()

