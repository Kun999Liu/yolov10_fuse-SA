import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

from ultralytics import YOLOv10
# from ultralytics import YOLO


if __name__ == '__main__':
    # 加载模型
    model = YOLOv10(
        r'.\ultralytics\run\v10m_fuse_6bands_windfram_500epochs\weights\best.pt')


    # 开始预测
    # model(source=r"F:\wxy_code\mydata\images\val", save=True)
    results = model.predict(source=r".\ultralytics\testimages",
                            imgsz=416,
                            cache='disk',
                            workers=8,
                            device='0',
                            exist_ok=False,
                            save=True,
                            #是否保存打印特征图
                            visualize=False,
                            name=r"D:\Git\yolov10_fuse\ultralytics\run\detect\pre"
                            )
