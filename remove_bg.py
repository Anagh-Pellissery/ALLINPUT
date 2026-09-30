import re
import base64
from io import BytesIO
from rembg import remove
from PIL import Image

def process_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    pattern = r'src="data:image/(jpeg|png|jpg);base64,([^"]+)"'
    
    def replacer(match):
        img_ext = match.group(1)
        base64_data = match.group(2)
        
        print(f"Decoding {img_ext} image...")
        image_data = base64.b64decode(base64_data)
        img = Image.open(BytesIO(image_data)).convert("RGBA")
        
        print("Removing background...")
        out_img = remove(img)
        
        print("Encoding back to base64...")
        buffered = BytesIO()
        out_img.save(buffered, format="PNG")
        new_base64_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        return f'src="data:image/png;base64,{new_base64_str}"'

    new_html = re.sub(pattern, replacer, html_content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Done!")

if __name__ == "__main__":
    process_html('index.html')
