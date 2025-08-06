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
│   ├── convert_16bit_to_8bit.py
│   ├── convert_24bit_to_8bit.py
├── model_testing/              # Inference using trained model
│   └── test_yolo.py
├── post_processing/            # Cropping predictions
│   └── crop_detected.py
├── yolo_format_conversion/     # Converts annotation to YOLO format
│   └── annotations_to_yolo.py
├── yolo_training/            # YOLOv8 training files
│   ├── train_yolo.py
│   ├── data.yaml
│   └── labels/
├── samples/                    # Sample images
│   ├── original_image.png
│   ├── converted_image.png
│   ├── annotated_image.png
│   ├── model_predicted.png
│   └── cropped_image.png
├── requirements.txt            # Python dependencies
└── README.md

````

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/stdynamicslab/ObjectDetection.git
cd ObjectDetection
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

1. **Convert Images to 8-bit**

   A. *Convert 16-bit images to 8-bit images*
   ```bash
   python image_conversion/convert_16bit_to_8bit.py --input_dir path/to/16bit_images --output_dir path/to/8bit_images
   ```
   B. *Convert 24-bit images to 8-bit images*
   ```bash
   python image_conversion/convert_24bit_to_8bit.py --input_dir path/to/24bit_images --output_dir path/to/8bit_images
   ```

3. **Annotate with Custom GUI**

   ```bash
   python annotation_tool/annotator_gui.py --input_dir path/to/8bit_images --output_dir path/to/annotated_images
   ```

4. **Convert Annotations to YOLO Format**

   ```bash
   python yolo_format_conversion/annotations_to_yolo.py
   ```

5. **Train YOLOv8 Model**

   ```bash
   python yolov5_training/train_yolo.py
   ```

6. **Run Detection on New Images**

   ```bash
   python model_testing/detect.py --weights path/to/best.pt --source path/to/test_images
   ```

7. **Crop Detected Circles**

   ```bash
   python post_processing/crop_detected.py --input path/to/predictions --output path/to/cropped
   ```

## 🖼️ Sample Output

Sample output images can be found in the `samples/` folder.



## 🙏 Acknowledgments

* [Ultralytics](https://github.com/ultralytics) for the YOLOv8 model

