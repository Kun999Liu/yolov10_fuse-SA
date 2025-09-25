import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

from ultralytics import YOLOv10
from ultralytics import YOLO


if __name__ == '__main__':
    # 加载模型
    # model = YOLOv10(r"G:\wanxingyu\project\yolov10\yolov10\ultralytics\cfg\models\v10\yolov10m.yaml")
    # model = YOLOv10(model=r'G:\wanxingyu\project\yolov10\yolov10-fuse\ultralytics\cfg\models\v5\yolov5m_fuse.yaml')
    model = YOLOv10(model=r'G:\wanxingyu\project\yolov10\yolov10-fuse\runs\detect\train-v10m-correct\weights\best.pt')
    # model = YOLOv10(r"G:\wanxingyu\project\yolov10\yolov10\ultralytics\cfg\models\v10\yolov10m.yaml")
    # model = YOLO(model=r'G:\wanxingyu\project\yolov10\yolov10-fuse\runs\detect\train-v8m-correct\weights\best.pt')
    # model = YOLO(model=r'G:\wanxingyu\project\yolov10\runs2\v5m\demo2\detect2\train\weights\best.pt')


    # 验证模型
    results = model.val(data="data.yaml",
                          resume=False,
                          epochs=100,
                          batch=1,
                          patience=30,
                          imgsz=416,
                          amp=False,
                          cache='disk',
                          workers=0,
                          device=0,
                          exist_ok=True,
                          # scale='m',
                          )
