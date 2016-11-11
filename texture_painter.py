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

def throw_invalid_selection():
    if len(bpy.context.selected_objects) == 0:
        raise Exception("Please select exactly one prorotype object.")
    if len(bpy.context.selected_objects) > 1:
        raise Exception("Please select exactly one prorotype object.")

def create_target_object(prototype, offset):
    prototype.select = True
    bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":offset})
    new_target_object = bpy.context.selected_objects[0]
    new_target_object.select = False # to leave selection "as found"
    return new_target_object

def get_offset(num, rows, spacing):
    """Return offset from prototype position.
    Positional arguments:
    num -- the number of the object, starting from 0
    rows -- how many rows before wrapping
    spacing -- a tuple of (x,y) spaing between objects
    """
    x_offset = (num % rows) * spacing[0] # x-spacing
    y_offset = (num // rows) * spacing[1] # y-spacing
    return (x_offset, y_offset)

def swap_texture_br(target_object, image_filename):
    """Swaps the first texture, on the first material to supplied
    This method is designed for Blender Render materials.
    """
    new_material = target_object.material_slots[0].material.copy()
    target_object.material_slots[0].material = new_material

    new_texture = new_material.texture_slots[0].texture.copy()
    new_material.texture_slots[0].texture = new_texture

    new_image = bpy.data.images.load(image_filename)
    new_texture.image = new_image

def swap_texture_cycles(target_object, image_filename):
    new_material = target_object.material_slots[0].material.copy()
    target_object.material_slots[0].material = new_material
    new_image = bpy.data.images.load(image_filename)
    new_material.node_tree.nodes['Image Texture'].image = new_image

def swap_text(target_object, backer, index):
    cwd = os.path.dirname(bpy.data.filepath)
    text_to_render = backer['Name'] + ', ' + backer['Country']
    filename = cwd + '\\texture_cache\\' + str(index) + '.png'
    render_text_to_file(text_to_render, filename)
    swap_texture_cycles(target_object, filename)

def go():
    print("Texture Painter starting up.")
    throw_invalid_selection()
    print("Prototype object found.")
    prototype = bpy.context.selected_objects[0]
    for num, backer in enumerate(get_backers('backers_10.csv')):
        if num == 0:
            target_object = prototype
        else:
            x, y = get_offset(num, 400, (-.5,.6,0))
            target_object = create_target_object(prototype, (x, y, 0))
        swap_text(target_object, backer, num)
