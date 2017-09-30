import imageio
import os
from landing import app

def stitch():

    images = []
    sort_names = []

    for filename in os.listdir(app.config["PROCESSING_DIRECTORY"]):
        if filename.endswith(app.config["INPUT_FILETYPE"]):
            sort_names.append(int(filename[:-(len(app.config["INPUT_FILETYPE"]))]))

    # this avoids that filename iteration problem with digits
    sort_names = sorted(sort_names)
    for file in sort_names:
            try:
                images.append(imageio.imread(app.config["PROCESSING_DIRECTORY"]+"/"+str(file)+app.config["INPUT_FILETYPE"]))
            except: 
                imageio.mimsave(app.config["OUTPUT_DIRECTORY"] + app.config["ATTEMPTED_OUTPUT_FILENAME"], images)

    imageio.mimsave(app.config["OUTPUT_DIRECTORY"] + app.config["OUTPUT_FILENAME"], images)
    return app.config["OUTPUT_FILENAME"]
    # current issue: https://github.com/imageio/imageio/issues/210