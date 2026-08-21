import sys
from PIL import Image

def make_transparent(input_path, output_path, tolerance=30):
    try:
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()
        
        # Get the background color from the top-left pixel
        bg_color = datas[0]
        
        newData = []
        for item in datas:
            # Check if the pixel is close to the background color
            if abs(item[0] - bg_color[0]) <= tolerance and \
               abs(item[1] - bg_color[1]) <= tolerance and \
               abs(item[2] - bg_color[2]) <= tolerance:
                newData.append((255, 255, 255, 0)) # Transparent
            else:
                newData.append(item)
                
        img.putdata(newData)
        img.save(output_path, "PNG")
        print(f"Successfully processed {input_path} and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python remove_bg.py <input> <output>")
    else:
        make_transparent(sys.argv[1], sys.argv[2])
