import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw
import os

class BatchAnnotator:
    def __init__(self, master, input_folder, output_folder):
        self.master = master
        self.master.title("Batch Rectangle Annotator")
        self.master.geometry("640x480")

        self.canvas = tk.Canvas(master, width=640, height=480, cursor="cross")
        self.canvas.pack()
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        self.input_folder = input_folder
        self.output_folder = output_folder
        self.images = sorted([
            f for f in os.listdir(input_folder)
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".tif", ".bmp"))
        ])
        self.index = 0

        btns = tk.Frame(master)
        btns.pack(fill=tk.X, side=tk.BOTTOM)
        tk.Button(btns, text="Previous", command=self.prev_image).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(btns, text="Next & Save", command=self.next_image).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(btns, text="Exit", command=self.master.quit).pack(side=tk.RIGHT, padx=5, pady=5)

        self.rect = None
        self.start_x = self.start_y = None
        self.orig_image = None
        self.display_image = None
        self.scale_x = self.scale_y = 1

        self.load_image()

    def load_image(self):
        if not (0 <= self.index < len(self.images)):
            messagebox.showinfo("Done", "All images processed!")
            self.master.quit()
            return

        fname = self.images[self.index]
        path = os.path.join(self.input_folder, fname)

        self.orig_image = Image.open(path)
        orig_w, orig_h = self.orig_image.size

        # For display only (always RGB)
        display_image = self.orig_image.convert("RGB").resize((640, 480))
        self.scale_x = orig_w / 640
        self.scale_y = orig_h / 480

        self.photo = ImageTk.PhotoImage(display_image)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.canvas.image = self.photo
        self.rect = None

    def on_press(self, event):
        self.start_x, self.start_y = event.x, event.y
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, event.x, event.y, outline="red", width=3
        )

    def on_drag(self, event):
        if self.rect:
            self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_release(self, event):
        if self.rect:
            self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def save_current(self):
        if self.rect:
            coords = list(map(int, self.canvas.coords(self.rect)))
            scaled_coords = [
                int(coords[0] * self.scale_x), int(coords[1] * self.scale_y),
                int(coords[2] * self.scale_x), int(coords[3] * self.scale_y)
            ]

            # Convert a copy to RGB just for drawing
            temp = self.orig_image.convert("RGB")
            draw = ImageDraw.Draw(temp)
            draw.rectangle(scaled_coords, outline="red", width=20)

            os.makedirs(self.output_folder, exist_ok=True)
            out_path = os.path.join(self.output_folder, self.images[self.index])
            # Save in original format
            temp.save(out_path, format=self.orig_image.format)

    def next_image(self):
        self.save_current()
        self.index += 1
        self.load_image()

    def prev_image(self):
        if self.index > 0:
            self.index -= 1
            self.load_image()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Batch Rectangle Annotator")
    parser.add_argument("--input_dir", required=True, help="Input folder path")
    parser.add_argument("--output_dir", required=True, help="Output folder path")
    args = parser.parse_args()

    if not os.path.exists(args.input_dir):
        messagebox.showerror("Error", f"Input folder not found: {args.input_dir}")
    else:
        root = tk.Tk()
        BatchAnnotator(root, args.input_dir, args.output_dir)
        root.mainloop()


