import pytesseract
from PIL import Image

def ocr_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    print(ocr_image('example.png'))
