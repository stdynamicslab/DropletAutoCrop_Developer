Circular Pattern Detection Using YOLOv8
A complete pipeline to detect and extract circular patterns from raw grayscale images using custom annotations and YOLOv8.

This project includes:
- Image bit-depth conversion (16/24-bit ➜ 8-bit)
- Custom GUI annotation tool
- Conversion to YOLO format
- Training a YOLOv8 model on circular patterns
- Cropping and saving detected circular regions
Project Structure
circle-detection-yolo/
├── image_conversion/           # 16/24-bit to 8-bit conversion
│   └── convert_to_8bit.py
├── annotation_tool/            # GUI for manual annotation
│   └── annotator_gui.py
├── yolo_format_conversion/     # Converts annotation to YOLO format
│   └── annotations_to_yolo.py
├── yolov5_training/            # YOLOv8 training files
│   ├── train_yolo.py
│   ├── data.yaml
│   └── labels/
├── model_testing/              # Inference using trained model
│   └── detect.py
├── post_processing/            # Cropping predictions
│   └── crop_detected.py
├── samples/                    # Sample images
│   ├── original_image.png
│   ├── annotation_view.png
│   ├── yolo_output.png
│   └── cropped_circle.png
├── requirements.txt            # Python dependencies
└── README.md
Installation
Clone the repository:
git clone https://github.com/yourusername/circle-detection-yolo.git
cd circle-detection-yolo

Create a virtual environment (optional):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt
Pipeline Overview
1. Convert Images
   python image_conversion/convert_to_8bit.py --input_dir path/to/raw_images --output_dir path/to/8bit_images

2. Annotate with Custom GUI
   python annotation_tool/annotator_gui.py --input_dir path/to/8bit_images

3. Convert Annotations to YOLO Format
   python yolo_format_conversion/annotations_to_yolo.py

4. Train YOLOv8 Model
   python yolov5_training/train_yolo.py

5. Run Detection on New Images
   python model_testing/detect.py --weights path/to/best.pt --source path/to/test_images

6. Crop Detected Circles
   python post_processing/crop_detected.py --input path/to/predictions --output path/to/cropped
Sample Output
Sample output images can be found in the 'samples/' folder.
Citation
@misc{yourname2025circledet,
  title={Circular Pattern Detection using YOLOv8},
  author={Your Name},
  year={2025},
  howpublished={\url{https://github.com/yourusername/circle-detection-yolo}},
}
License
This project is licensed under the MIT License.
Acknowledgments
• Ultralytics for the YOLOv8 model
• Any lab, guide, or funding source (e.g., SERB, CSIR)
