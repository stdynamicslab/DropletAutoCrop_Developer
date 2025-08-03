import os
import cv2
import numpy as np

def convert_24bit_to_8bit_png(input_path, output_path):
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        print(f"Failed to load: {input_path}")
        return

    # Skip non-8-bit-3-channel images
    if img.dtype != np.uint8 or img.ndim != 3 or img.shape[2] != 3:
        print(f"Skipping (not 24‑bit RGB): {input_path}")
        return

    # Convert BGR to 8-bit grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Ensure PNG
    output_path = os.path.splitext(output_path)[0] + ".png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, gray)
    print(f"Saved: {output_path}")

def process_folder(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('.tif', '.tiff', '.png', '.jpg', '.jpeg', '.bmp')):
                input_path = os.path.join(root, file)
                rel_path = os.path.relpath(input_path, input_folder)
                output_path = os.path.join(output_folder, rel_path)
                convert_24bit_to_8bit_png(input_path, output_path)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Convert 24-bit RGB images to 8-bit grayscale PNGs")
    parser.add_argument("input_folder", help="Input folder path")
    parser.add_argument("output_folder", help="Output folder path")
    args = parser.parse_args()

    process_folder(args.input_folder, args.output_folder)
