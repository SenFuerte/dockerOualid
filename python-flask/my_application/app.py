from flask import Flask
from flask import request
import os, sys
app = Flask(__name__)

path = "./uploads/"
dirs = os.listdir( path )


@app.route("/")
def hello():
    return "Hello World!"

def goodBye():
    return "Good Bye World!"

def itRuns():
    return "It runs"


@app.route("/list")
def listfile():
   for file in dirs:
    return file


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
