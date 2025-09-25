import os

def extract_fields_from_filenames(root_folder, output_txt):
    results = set()

    for folder_path, _, files in os.walk(root_folder):  # 遍历所有子目录和文件
        for filename in files:
            name, _ = os.path.splitext(filename)  # 去掉扩展名
            parts = name.split('-')
            if len(parts) >= 3:        # 有两个及以上 '-'
                field = '-'.join(parts[:2])   # 保留第二个 '-' 前
            elif len(parts) == 2:      # 只有一个 '-'
                field = parts[0]
            else:                      # 没有 '-'
                field = parts[0]
            results.add(field)

    # 保存去重结果
    with open(output_txt, 'w', encoding='utf-8') as f:
        for item in sorted(results):
            f.write(item + '\n')

if __name__ == "__main__":
    folder = r"C:\Users\liuku\Desktop\野生虫草2025\野生虫草2025"  # 修改为你的文件夹路径
    output_file = r"C:\Users\liuku\Desktop\野生虫草.txt" # 输出 txt 文件路径
    extract_fields_from_filenames(folder, output_file)
    print("处理完成，结果已保存到:", output_file)
