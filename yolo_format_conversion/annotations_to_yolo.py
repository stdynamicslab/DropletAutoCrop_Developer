import cv2
import numpy as np
import os

def extract_bboxes_from_annotated_image(img_path, output_label_path):
    # Load image
    img = cv2.imread(img_path)
    if img is None:
        print(f"Failed to load image {img_path}")
        return

    height, width = img.shape[:2]

    # Convert to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define red color ranges in HSV
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    # Threshold the HSV image to get only red colors
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Optional: Morphological operations to clean noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

    # Find contours (red squares)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # List to store YOLO labels: class x_center y_center width height (normalized)
    yolo_labels = []

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Filter small regions (noise)
        if w < 10 or h < 10:
            continue

        # Convert to YOLO format (normalized)
        x_center = (x + w / 2) / width
        y_center = (y + h / 2) / height
        w_norm = w / width
        h_norm = h / height

        class_id = 0  # assuming one class "droplet"

        yolo_labels.append(f"{class_id} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}")

    # Save YOLO labels to txt file
    with open(output_label_path, 'w') as f:
        for line in yolo_labels:
            f.write(line + '\n')

    print(f"Saved {len(yolo_labels)} bounding boxes to {output_label_path}")


def process_folder(annotated_images_folder, labels_output_folder):
    if not os.path.exists(labels_output_folder):
        os.makedirs(labels_output_folder)

    for filename in os.listdir(annotated_images_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff')):
            img_path = os.path.join(annotated_images_folder, filename)
            label_filename = os.path.splitext(filename)[0] + '.txt'
            label_path = os.path.join(labels_output_folder, label_filename)

            extract_bboxes_from_annotated_image(img_path, label_path)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert red rectangles in annotated images to YOLO format")
    parser.add_argument("--input_dir", required=True, help="Path to folder containing red-rectangle annotated images")
    parser.add_argument("--output_dir", required=True, help="Path to save YOLO-format .txt label files")
    args = parser.parse_args()

    process_folder(args.input_dir, args.output_dir)

