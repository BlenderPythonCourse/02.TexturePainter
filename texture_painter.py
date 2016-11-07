'''Renders text from a CSV file to textures
and applies them to multiple objects.

Use snippets...
import os, sys; sys.path.append(os.path.dirname(bpy.data.filepath)); import texture_painter
import importlib; importlib.reload(texture_painter); texture_painter.go()
'''

import codecs
import csv
from PIL import Image, ImageFont, ImageDraw
import os
import bpy

def get_backers(csv_filename):
    with codecs.open(csv_filename, 'r', 'utf-8-sig') as stream:
        iterable = csv.reader(stream)
        header = next(iterable)
        for row in iterable:
            backer = dict(zip(header, row))
            yield backer

# image size and font-size hard-coded in method
def render_text_to_file(text_to_render, to_filename):
    image = Image.new('RGB', (512,64))
    draw = ImageDraw.Draw(image)
    fnt = ImageFont.truetype('arial.ttf', 50)
    draw.text((0,0), text_to_render, font=fnt, fill=(255,255,255))
    image.save(to_filename)

def read_csv():
    # Read through the CSV
    cwd = os.path.dirname(bpy.data.filepath)
    for backer in get_backers('backers_10.csv'):
        text_to_render = backer['Name'] + ', ' + backer['Country']
        filename = cwd + '\\texture_cache\\' + backer['Number'] + '.png'
        print("Rendering", text_to_render, "to", filename)
        render_text_to_file(text_to_render, filename)

def throw_invalid_selection():
    if len(bpy.context.selected_objects) == 0:
        raise Exception("Please select exactly one prorotype object.")
    if len(bpy.context.selected_objects) > 1:
        raise Exception("Please select exactly one prorotype object.")

def create_plaque(prototype, offset):
    prototype.select = True
    bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":offset})
    new_plaque = bpy.context.selected_objects[0]
    new_plaque.select = False # to leave selection "as found"
    return new_plaque

def go():
    print("Texture Painter starting up.")
    throw_invalid_selection()
    print("Prototype object found.")
    # read_csv()

    prototype = bpy.context.selected_objects[0]
    create_plaque(prototype, (0,1,0))
