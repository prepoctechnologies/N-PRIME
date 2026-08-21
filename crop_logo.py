import sys
from PIL import Image

def process(input_path, output_path):
    try:
        img = Image.open(input_path).convert("RGBA")
        
        # Crop to bounding box of non-transparent pixels
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
            
        img.save(output_path, "PNG")
        print(f"Saved cropped white logo to {output_path}")
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python crop_logo.py <input> <output>")
    else:
        process(sys.argv[1], sys.argv[2])
