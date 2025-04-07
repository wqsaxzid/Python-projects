import pytesseract
from PIL import Image

img = Image.open('./img/phone_number.png')
pytesseract.pytesseract.tesseract_cmd = r'C:/Games/tesseract.exe'

custom_config = r'--oem 3 --psm 13'

text = pytesseract.image_to_string(img, config=custom_config)
print(text)

with open('phone_number.txt', 'w') as text_file:
    text_file.write(text)