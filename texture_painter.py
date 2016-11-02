'''Renders text from a CSV file to textures
and applies them to multiple objects.

Use snippets...
import os, sys; sys.path.append(os.path.dirname(bpy.data.filepath)); import texture_painter
import importlib; importlib.reload(texture_painter); texture_painter.go()
'''

import codecs

def get_backers(csv_filename):
    stream = codecs.open(csv_filename, 'r', 'utf-8-sig')
    return stream  # change to backer object later

def go():
    print("Texture Painter starting up.")
    # Read through the CSV
    print(get_backers('backers_10.csv'))
