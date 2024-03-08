# -*- coding: utf-8 -*-
from flask import Flask, request
import tarfile
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './uploads'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024
ALLOWED_EXTENSIONS = {'tar'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    with open(__file__, 'r') as f:
        return f.read()


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return '?'
    file = request.files['file']
    if file.filename == '':
        return '?'
    print(file.filename)
    if file and allowed_file(file.filename):  # and '..' not in file.filename and '/' not in file.filename
        file_save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        if os.path.exists(file_save_path):
            return 'This file already exists'
        file.save(file_save_path)
    else:
        return 'This file is not a tarfile'
    try:
        tar = tarfile.open(file_save_path, "r")
        tar.extractall(app.config['UPLOAD_FOLDER'])
    except Exception as e:
        return str(e)
    os.remove(file_save_path)
    return 'success'


@app.route('/download', methods=['POST'])
def download_file():
    filename = request.form.get('filename')
    if filename is None or filename == '':
        return '?'
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if '..' in filename or '/' in filename:
        return '?'
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        return '?'
    with open(filepath, 'r') as f:
        return f.read()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
