from flask import Flask
from flask import request
import os
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"
@app.route("/euler1")
def eulerOne():
    n = 1000
    result = 0
    for x in range(1,n):
	if( x % 3 == 0) or (x % 5 == 0):
		result = result + x
    return str(result)

def fibbo(x):
	if(x == 0):
		return 0
	elif x == 1:
		return 1
	else:
		return (fibbo(x-1) + fibbo(x-2))

@app.route("/euler2")
def eulerTwo():
	for z in range(1,1000):
		if( fibbo(z) >= 4000000):
			return str((z-1))


@app.route("/list")
def listfile():
   path = "./uploads/"
   folder = os.listdir(path)
   filelist = ""
   for file in folder:
    filelist += file + "/n"
   return filelist


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
