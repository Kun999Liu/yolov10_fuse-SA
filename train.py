import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
os.environ['GTIFF_SRS_SOURCE'] = 'EPSG'

import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLOv10
from ultralytics import YOLO

if __name__ == '__main__':
    # 加载模型
    # model = YOLOv10(r"G:\wanxingyu\project\yolov10\yolov10\ultralytics\cfg\models\v10\yolov10m.yaml").load('yolov10m.pt')
    model = YOLOv10(r"F:\wxy_code\yolov10-fuse-SA\ultralytics\cfg\models\v10\yolov10m_fuse_ndsi_C3k2_DEAB.yaml")
    # model = YOLO(r'G:\wanxingyu\project\yolov10\yolov10-fuse\ultralytics\cfg\models\v10\yolov10m_fuse_noPSA.yaml')

    # 训练模型
    results = model.train(data="./data.yaml",
                          resume=True,
                          epochs=1,
                          batch=16,
                          patience=30,
                          imgsz=416,
                          amp=False,
                          cache='disk',
                          workers=0,
                          device=0,
                          exist_ok=True,
                          # scale='m',
                          name="train_C3k2_DEAB_test_7bands"
                          )
