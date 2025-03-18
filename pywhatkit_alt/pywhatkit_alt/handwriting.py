from PIL import Image, ImageDraw, ImageFont

def text_to_handwriting(text, output="handwriting.png"):
    img = Image.new("RGB", (500, 200), color="white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()  # Load handwriting-style font
    draw.text((50, 50), text, fill="black", font=font)
    img.save(output)
