import sys
from PIL import Image

def process(input_path, output_path):
    try:
        img = Image.open(input_path).convert("RGBA")
        
        # 1. Convert white pixels to black
        datas = img.getdata()
        newData = []
        for item in datas:
            # Check if pixel is white-ish (R, G, B all > 200) and not fully transparent
            if item[3] > 0 and item[0] > 200 and item[1] > 200 and item[2] > 200:
                # Change to black, keep same alpha
                newData.append((0, 0, 0, item[3]))
            else:
                newData.append(item)
                
        img.putdata(newData)
        
        # 2. Crop to bounding box of non-transparent pixels
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
            
        img.save(output_path, "PNG")
        print(f"Saved processed logo to {output_path}")
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python process_logo.py <input> <output>")
    else:
        process(sys.argv[1], sys.argv[2])
