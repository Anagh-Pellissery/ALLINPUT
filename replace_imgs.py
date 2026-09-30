import re

def replace_images():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = re.sub(r'<img class="logo" src="data:[^"]+"', '<img class="logo" src="logo-removebg-preview.png"', content)
    content = re.sub(r'<img class="car" src="data:[^"]+"', '<img class="car" src="car-removebg-preview.png"', content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    replace_images()
