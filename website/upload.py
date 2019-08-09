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
def upload_file():
    if request.method == 'POST':
        lost_or_found = request.form.get('lost_found')
        pet = request.form.get('pet')
        location = request.form.get('location')
        date = request.form.get('date')
        color = request.form.get('color')
        addit_info = request.form.get('addit_info')
    
        files = request.files.getlist('files[]')
        for file in files:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        return '''
                Upload completed. <br> 
                <br>
                Lost or found: {} <br>
                Pet: {} <br>
                Location: {} <br>
                Date: {} <br>
                Color is {} <br>
                Addit info: {} <br>
               '''.format(lost_or_found, pet, location, date, color, addit_info)
    return render_template('upload.html')



if __name__ == '__main__':
    app.run(debug=True)

