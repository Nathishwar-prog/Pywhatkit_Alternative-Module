from PIL import Image

def image_to_ascii(image_path):
    img = Image.open(image_path).convert("L")  # Convert to grayscale
    width, height = img.size
    img = img.resize((width // 10, height // 10))  # Resize for ASCII
    chars = "@%#*+=-:. "
    ascii_str = ""
    for pixel in img.getdata():
        ascii_str += chars[pixel // 25]
    return ascii_str
