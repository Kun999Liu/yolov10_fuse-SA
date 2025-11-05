import importlib
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

from ultralytics.models.yolov10.model import YOLOv10
from ultralytics import YOLO

if __name__ == '__main__':
    # 加载模型
    model = YOLOv10(
        r'.\ultralytics\run\v10m_fuse_6bands_windfram_500epochs\weights\best.pt')


    # 开始预测
    # model(source=r"F:\wxy_code\mydata\images\val", save=True)
    results = model.predict(source=r".\ultralytics\testimages",
                            imgsz=416,
                            cache='disk',
                            workers=0,
                            device='0',
                            exist_ok=False,
                            save=True,
                            visualize=False,
                            name=r".\ultralytics\run\detect\pre"
                            )
