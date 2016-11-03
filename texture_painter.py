'''Renders text from a CSV file to textures
and applies them to multiple objects.

Use snippets...
import os, sys; sys.path.append(os.path.dirname(bpy.data.filepath)); import texture_painter
import importlib; importlib.reload(texture_painter); texture_painter.go()
'''

import codecs
import csv
from PIL import Image, ImageFont, ImageDraw

def get_backers(csv_filename):
    with codecs.open(csv_filename, 'r', 'utf-8-sig') as stream:
        iterable = csv.reader(stream)
        header = next(iterable)
        for row in iterable:
            backer = dict(zip(header, row))
            yield backer

# image size and font-size hard-coded in method
def render_text_to_file(text_to_render):
    image = Image.new('RGB', (128,128))
    draw = ImageDraw.Draw(image)
    fnt = ImageFont.truetype('arial.ttf', 50)
    draw.text((0,0), text_to_render, font=fnt, fill=(255,255,255))
    image.save("test.png")

def go():
    print("Texture Painter starting up.")
    # Read through the CSV
    for backer in get_backers('backers_10.csv'):
        render_text_to_file("It worked!")
