import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

from ultralytics import YOLOv10
# from ultralytics import YOLO


if __name__ == '__main__':
    # 加载模型
    model = YOLOv10(
        r'D:\Git\yolov10_fuse-SA\ultralytics\run\fuse_ndsi_windfram\weights\best.pt')


    # 开始预测
    # model(source=r"F:\wxy_code\mydata\images\val", save=True)
    results = model.predict(source=r"D:\yolodatasets\testdatasets\images\test",
                            imgsz=416,
                            cache='disk',
                            workers=0,
                            device='cpu',
                            exist_ok=False,
                            save=True,
                            #是否保存打印特征图
                            visualize=False,
                            name=r"D:\Git\yolov10_fuse-SA\ultralytics\run\detect\pre"
                            )
