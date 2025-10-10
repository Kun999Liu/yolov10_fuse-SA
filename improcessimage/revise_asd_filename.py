# -*- coding: utf-8 -*-
# @Time    : 2025/7/26 20:47
# @Author  : Liu Kun
# @Email   : liukunjsj@163.com
# @File    : revise_asd_filename.py
# @Software: PyCharm

"""
Describe:
"""
import os

def rename_all_files_globally(root_dir, group_size=20):
    # 收集所有子文件夹下的文件路径
    all_files = []
    for root, _, files in os.walk(root_dir):
        for f in files:
            all_files.append(os.path.join(root, f))

    all_files.sort()  # 全局排序

    for i in range(0, len(all_files), group_size):
        group_number = (i // group_size) + 1
        group_files = all_files[i:i + group_size]

        for idx, file_path in enumerate(group_files, start=1):
            folder_path = os.path.dirname(file_path)
            filename = os.path.basename(file_path)
            name, ext = os.path.splitext(filename)

            new_name = f"group{group_number:03}_{idx:02}{ext}"
            new_path = os.path.join(folder_path, new_name)

            # 防止重名
            counter = 1
            while os.path.exists(new_path):
                new_name = f"group{group_number:03}_{idx:02}_{counter}{ext}"
                new_path = os.path.join(folder_path, new_name)
                counter += 1

            os.rename(file_path, new_path)
            print(f"[{os.path.basename(folder_path)}] {filename} → {new_name}")

def rename_files_in_folder(folder_path):
    # 收集当前文件夹下的所有文件（不包括子文件夹）
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # 按文件名排序
    files.sort()

    # 遍历并重命名
    for idx, filename in enumerate(files, start=1):
        file_path = os.path.join(folder_path, filename)
        name, ext = os.path.splitext(filename)

        # 删除第一个 '_' 前的内容
        if '-' in name:
            _, rest = name.split('-', 1)
            new_name = f"{idx:03}-{rest}{ext}"
        else:
            new_name = f"{idx:03}-{name}{ext}"

        new_path = os.path.join(folder_path, new_name)

        # 防止重名
        counter = 1
        while os.path.exists(new_path):
            if '-' in name:
                _, rest = name.split('-', 1)
                new_name = f"{idx+1:03}-{rest}{ext}"
            else:
                new_name = f"{idx+1:03}-{name}{ext}"
            new_path = os.path.join(folder_path, new_name)
            counter += 1

        os.rename(file_path, new_path)
        print(f"[{os.path.basename(folder_path)}] Renamed: {filename} -> {new_name}")


def batch_rename_multiple_folders(root_dir):
    # 自动遍历root_dir下的所有子文件夹
    for subdir in os.listdir(root_dir):
        dir_path = os.path.join(root_dir, subdir)
        if os.path.isdir(dir_path):
            print(f"\nProcessing folder: {dir_path}")
            rename_files_in_folder(dir_path)


# 使用示例
root_directory = r"C:\Users\liuku\Desktop\asd" # 替换为你的主文件夹路径
rename_files_in_folder(root_directory)