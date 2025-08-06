from ultralytics import YOLO
import multiprocessing

def main():
    model = YOLO('yolov8n.pt')  # Load YOLOv8 nano model
    model.train(
        data='data.yaml',      # Path to dataset YAML
        epochs=50,             # Number of training epochs
        imgsz=640,             # Image resolution
        batch=2,               # Batch size (adjust for GPU/CPU)
        device=0               # Use GPU 0; set to 'cpu' if no GPU
    )

if __name__ == '__main__':
    multiprocessing.freeze_support()  # For compatibility with Windows
    main()
