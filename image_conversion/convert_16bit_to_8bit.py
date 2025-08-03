import os
import cv2
import numpy as np

def convert_16bit_to_8bit_png(input_path, output_path):
    img_16bit = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    if img_16bit is None:
        print(f"Failed to load: {input_path}")
        return

    if img_16bit.dtype != np.uint16:
        print(f"Skipping (not 16-bit): {input_path}")
        return

    # Normalize and convert to 8-bit
    img_8bit = cv2.normalize(img_16bit, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')

    # Change output extension to .png
    output_path = os.path.splitext(output_path)[0] + ".png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, img_8bit)
    print(f"Saved: {output_path}")

def process_folder(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('.tif', '.tiff')):
                input_path = os.path.join(root, file)
                rel_path = os.path.relpath(input_path, input_folder)
                output_path = os.path.join(output_folder, rel_path)
                convert_16bit_to_8bit_png(input_path, output_path)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert 16-bit TIFFs to 8-bit PNGs")
    parser.add_argument("input_folder", help="Input folder path")
    parser.add_argument("output_folder", help="Output folder path")
    args = parser.parse_args()

    process_folder(args.input_folder, args.output_folder)