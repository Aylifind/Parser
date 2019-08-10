from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/user/Desktop/website/database_files/filesstorage.db'
db = SQLAlchemy(app)


class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))   # 300 - максимальная длина строки
    data = db.Column(db.LargeBinary)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    db.create_all()   # создать базу данных

    lost_or_found = request.form.get('lost_found')
    pet = request.form.get('pet')
    location = request.form.get('location')
    date = request.form.get('date')
    color = request.form.get('color')
    addit_info = request.form.get('addit_info')
    files = request.files.getlist('files[]')


    for file in files:
        newFile = Clients(name=file.filename, data=file.read())
        db.session.add(newFile)
        db.session.commit()

        return '''
                Upload completed. <br> 
                <br>
                <b>File saved: {}</b> <br>
                Lost or found: {} <br>
                Pet: {} <br>
                Location: {} <br>
                Date: {} <br>
                Color: {} <br>
                Addit info: {} <br>
               '''.format(file.filename, lost_or_found, pet, location, date, color, addit_info)
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
