
from ultralytics import YOLO
import os

# === CONFIG ===
model_path = 'runs/detect/train/weights/best.pt'  # or last.pt
input_path = r'test_dataset\images\test_images'  # folder OR image file OR video file
output_dir = 'runs/detect/predict'  # will be auto-created

# === LOAD MODEL ===
model = YOLO(model_path)

# === RUN INFERENCE ===
results = model(input_path, save=True, save_txt=True, save_conf=True)

# === OPTIONAL: Show Results
for r in results:
    r.show()  # opens the image with boxes



# from ultralytics import YOLO

# # Load trained model weights (replace with your path)
# model = YOLO(r'yolov8n.pt')

# # Run inference on test images folder and save results
# results = model.predict(source='dataset/images/test',
#                         imgsz=960,
#                         conf=0.25,
#                         save=True,
#                         save_txt=True)

# print("Inference complete, results saved.")


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

