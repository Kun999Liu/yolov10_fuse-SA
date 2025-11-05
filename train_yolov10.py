import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ['GTIFF_SRS_SOURCE'] = 'EPSG'
import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLOv10

if __name__ == '__main__':
    # 加载模型
    # model = YOLOv10(r"G:\wanxingyu\project\yolov10\yolov10\ultralytics\cfg\models\v10\yolov10m.yaml").load('yolov10m.pt')
    # model = YOLOv10(r"D:\OneDrive_files\OneDrive\code\yolov10_fuse-SA\ultralytics\cfg\models\v10\yolov10m_fuse_ndsi_C3k2_DEAB.yaml")
    model = YOLOv10(
        r".\yolov10m_fuse.yaml")
    # model = YOLO(r'G:\wanxingyu\project\yolov10\yolov10-fuse\ultralytics\cfg\models\v10\yolov10m_fuse_noPSA.yaml')

    # 训练模型
    results = model.train(data="./data.yaml",
                          resume=True,
                          epochs=500,
                          batch=16,
                          patience=80,
                          imgsz=416,
                          amp=False,
                          workers=8,
                          device='0',
                          exist_ok=True,
                          # scale='m',
                          name=r"D:\Git\yolov10_fuse\ultralytics\run\v10m_fuse_6bands_windfram_500epochs"
                          )
"""测试git"""

# import sys
# import torch
#
# # Python 版本
# print("Python Version:", sys.version)
#
# # PyTorch 版本
# print("PyTorch Version:", torch.__version__)
#
# # CUDA 可用性
# print("CUDA Available:", torch.cuda.is_available())
#
# # CUDA 设备数量
# print("Number of CUDA devices:", torch.cuda.device_count())
#
# # 每个 CUDA 设备信息
# for i in range(torch.cuda.device_count()):
#     print(f"Device {i}: {torch.cuda.get_device_name(i)}")
#
# # PyTorch 编译时 CUDA 版本
# print("PyTorch CUDA Version:", torch.version.cuda)
# '''测试git上传'''
