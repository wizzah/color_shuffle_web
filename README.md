# color_shuffle_web

Local set up is similar to the non-web version - https://github.com/wizzah/color_shuffle
Except, instead of running the scripts to split, process, and stitch the gif, run flask - 
```
export FLASK_APP=app.py
flask run
```
then go to localhost:5000 in your browser. That's it!
There is also code in this project to clear the processing folder between uploads.
