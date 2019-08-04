from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os


UPLOAD_FOLDER = './static/uploads'    # папка, куда будут загружаться файлы с сайта
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
    	files = request.files.getlist('files[]')
    	for file in files:
    		file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    	return 'Upload completed.'
    return render_template('upload.html')


if __name__ == '__main__':
	app.run(debug=True)

