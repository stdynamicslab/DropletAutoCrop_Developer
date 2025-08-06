# Circular Pattern Detection Using YOLOv8

A complete pipeline to detect and extract circular patterns from raw grayscale images using custom annotations and YOLOv8.

## 🔍 Features

This project includes:
- Image bit-depth conversion (16/24-bit ➜ 8-bit)
- Custom GUI annotation tool
- Conversion to YOLO format
- Training a YOLOv8 model on circular patterns
- Cropping and saving detected circular regions

## 📁 Project Structure

```

//

ObjectDetection/
├── annotation_tool/            # GUI for manual annotation
│   └── annotator_gui.py
├── image_conversion/           # 16/24-bit to 8-bit conversion
│   └── convert_to_8bit.py
├── model\_testing/              # Inference using trained model
│   └── detect.py
├── post\_processing/            # Cropping predictions
│   └── crop\_detected.py
├── yolo_format_conversion/     # Converts annotation to YOLO format
│   └── annotations\_to\_yolo.py
├── yolo_training/            # YOLOv8 training files
│   ├── train_yolo.py
│   ├── data.yaml
│   └── labels/
├── samples/                    # Sample images
│   ├── original\_image.png
│   ├── annotation\_view\.png
│   ├── yolo\_output.png
│   └── cropped\_circle.png
├── requirements.txt            # Python dependencies
└── README.md

````

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/circle-detection-yolo.git
cd circle-detection-yolo
````

Create a virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔄 Pipeline Overview

1. **Convert Images**

   ```bash
   python image_conversion/convert_to_8bit.py --input_dir path/to/raw_images --output_dir path/to/8bit_images
   ```

2. **Annotate with Custom GUI**

   ```bash
   python annotation_tool/annotator_gui.py --input_dir path/to/8bit_images
   ```

3. **Convert Annotations to YOLO Format**

   ```bash
   python yolo_format_conversion/annotations_to_yolo.py
   ```

4. **Train YOLOv8 Model**

   ```bash
   python yolov5_training/train_yolo.py
   ```

5. **Run Detection on New Images**

   ```bash
   python model_testing/detect.py --weights path/to/best.pt --source path/to/test_images
   ```

6. **Crop Detected Circles**

   ```bash
   python post_processing/crop_detected.py --input path/to/predictions --output path/to/cropped
   ```

## 🖼️ Sample Output

Sample output images can be found in the `samples/` folder.



## 🙏 Acknowledgments

* [Ultralytics](https://github.com/ultralytics) for the YOLOv8 model

