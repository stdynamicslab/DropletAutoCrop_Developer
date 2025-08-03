from ultralytics import YOLO
import multiprocessing

def main():
    model = YOLO('yolov8n.pt')
    model.train(
        data='data.yaml',
        epochs=50,
        imgsz=640,
        batch=2,
        device=0
    )

if __name__ == '__main__':
    multiprocessing.freeze_support()  # <-- Required on Windows
    main()



# from ultralytics import YOLO

# model = YOLO('yolov8n.pt')  # or yolov8s.pt, yolov8m.pt, etc.
# model.train(data='data.yaml', epochs=50, imgsz=640, batch=2, device=0)



# from ultralytics import YOLO

# model = YOLO('yolov8n.pt')  # use the small pretrained model as starting point

# model.train(data='data.yaml', epochs=50, imgsz=960, batch=4)  
# # batch size 4 or lower since you have few images and likely limited GPU


# from ultralytics import YOLO

# def main():
#     model = YOLO('yolov8n.pt')
#     model.train(
#         data='data.yaml',
#         epochs=50,
#         imgsz=960,       # or reduce to 768 or 640
#         batch=2,         # try 1 if it still freezes
#         device=0
#     )

# if __name__ == '__main__':
#     main()


