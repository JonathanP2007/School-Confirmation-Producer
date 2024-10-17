import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

current_time = datetime.now().strftime("%H:%M")
current_date = datetime.now().strftime("%d/%m/%Y")

def reversetext(text):
    new_text = ""
    for i in range(len(text)):
        new_text = new_text + text[len(text) - 1 - i]
    return new_text

image_path = 'iphonedefault.jpg'
image = Image.open(image_path)

draw = ImageDraw.Draw(image)

shem = reversetext(input("מה השם? "))
kita = reversetext(input("מה הכיתה? "))
kita_number = input("איזה מספר כיתה? ")
#shaa = input("איזה שעה? ")
if input("לבחור שעה בעצמך? (y/n) ") == "y":
    shaa = input("איזה שעה? ")
else:
    shaa = current_time
if input("לבחור תאריך בעצמך? (y/n) ") == "y":
    taarich = input("איזה תאריך? ")
else:
    taarich = current_date
if input("לבחור שעה נוכחית בעצמך? (y/n) ") == "y":
    time = input("איזה שעה? ")
else:
    time = current_time

font_path = "Alef-bold.ttf"
number_font_path = "Roboto-Bold.ttf"
font_size = 30
number_size = 28
shaa_size = 29
time_size = 38
font = ImageFont.truetype(font_path, font_size)
number_font = ImageFont.truetype(number_font_path, number_size)
shaa_font = ImageFont.truetype(number_font_path, shaa_size)
time_font = ImageFont.truetype(number_font_path, time_size)

# Calculate text bounding box
shembox = draw.textbbox((0, 0), shem, font=font)
shem_width = shembox[2] - shembox[0]  # Width of the text

kitabox = draw.textbbox((0, 0), kita, font=font)
kita_width = kitabox[2] - kitabox[0]  # Width of the text

kita_numberbox = draw.textbbox((0, 0), kita_number, font=number_font)
kita_number_width = kita_numberbox[2] - kita_numberbox[0]  # Width of the text

# Define text position (adjust as needed)
image_width, image_height = image.size
shem_position = (image_width - shem_width - 215, 358)
kita_position = (image_width - kita_width - 640, 354)
if len(kita) != 1:
    kita_number_position = (image_width - kita_number_width - 671, 364)
else:
    kita_number_position = (image_width - kita_number_width - 652, 364)
shaa_position = (57, 287)
taarich_position = (440, 287)
time_position = (63, 32)

text_color = (0, 0, 0)

draw.text(shem_position, shem, font=font, fill=text_color)
draw.text(kita_position, kita, font=font, fill=text_color)
draw.text(kita_number_position, kita_number, font=number_font, fill=text_color)
draw.text(shaa_position, shaa, font=shaa_font, fill=text_color)
draw.text(taarich_position, taarich, font=number_font, fill=text_color)
draw.text(time_position, time, font=time_font, fill=text_color)

output_path = reversetext(shem) + '.jpg'
image.save(output_path)

print(f"Image saved as {output_path}")
