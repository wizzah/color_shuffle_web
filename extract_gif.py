import os
from PIL import Image
from landing import app

def extract_gif(gif):
    frame = Image.open(gif)
    nframes = 0
    while frame:
        frame.save( '%s/%s%s' % (app.config["PROCESSING_DIRECTORY"], nframes, app.config["INPUT_FILETYPE"]) , 'GIF')
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break;
    return True

