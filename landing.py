from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import extract_gif
import process
import stitch
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/upload", methods=['GET', 'POST'])
def img_upload():
    if request.method == 'POST':
        print("got here")
        gif = request.files["uploaded"]
        print("gif")
        extract_gif.extract_gif(gif)
        print("extracted")
        process.process_gif()
        print("process done")
        output = stitch.stitch()
        # return send_file(result, 'image/gif')
        print("output done")
        print(gif)
        print(output)
        return render_template('test.html', output=output, input=gif)

