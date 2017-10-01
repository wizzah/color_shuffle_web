from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import os
import config

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

import extract_gif
import process
import stitch
import pdb

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/upload", methods=['GET', 'POST'])
def img_upload():
    if request.method == 'POST':
        gif = request.files["uploaded"]
        app.config['INPUT_FILENAME'] = gif.filename
        app.config['OUTPUT_FILENAME'] = "output_"+gif.filename

        # create output and processing if they don't exist
        if not os.path.exists(app.config["OUTPUT_DIRECTORY"]):
            os.makedirs(app.config["OUTPUT_DIRECTORY"])

        if not os.path.exists(app.config["PROCESSING_DIRECTORY"]):
            os.makedirs(app.config["PROCESSING_DIRECTORY"])

        # save input gif to the output folder so we can show the user
        gif.save(app.config["OUTPUT_DIRECTORY"] + "/" + gif.filename)

        extract_gif.extract_gif(gif)
        process.process_gif()
        output = stitch.stitch()
        return render_template('result.html', output=output, input=gif.filename)


if __name__ == '__main__':
  app.run()