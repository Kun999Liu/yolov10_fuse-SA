# -*- coding: utf-8 -*-
# @Time    : 2025/5/19 10:42
# @Author  : Liu Kun
# @Email   : liukunjsj@163.com
# @File    : imagechannle_test.py
# @Software: PyCharm

"""
Describe:
"""
import numpy as np

# 假设文件名为 'data.npy'
file_path = r"D:\yolodatasets\windturbine_6bands\images\train\GF2_PMS1_E82.7_N45.2_20220430_L1A0006441524-pansharpen2colNum_12rowNum_39.npy"

# 加载 .npy 文件
data = np.load(file_path)

# 打印数组的形状
print("数组的形状:", data.shape)

# 检查是否至少有三个维度
if len(data.shape) >= 3:
    # 假设第三个维度是通道数
    channels = data.shape[2]
    print("通道数:", channels)
else:
    print("该数组没有通道维度，或不是多维数组")
