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
        extract_gif.extract_gif(gif)
        process.process_gif()
        output = stitch.stitch()
        return render_template('test.html', output=output, input=gif.filename)

