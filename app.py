import os
import shutil
from flask import Flask, render_template, request, redirect, send_from_directory, jsonify
from werkzeug import secure_filename
import os.path
from pdf2image import convert_from_path
import glob



# Initialize the Flask application
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['TEXT_OUT'] = 'textout/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg','pdf'])

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html')

path = app.config['UPLOAD_FOLDER']
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded files
    uploaded_files = request.files.getlist("file[]")
    filenames = []
    for file in uploaded_files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.rename(os.path.join(path,filename),os.path.join(path,'dst.pdf'))

            filenames.append(filename)
            PDF_file = path+'dst.pdf'
            pages = convert_from_path(PDF_file, 500)
            for page in pages:
                filename = "page_.jpg"
                page.save(filename, 'JPEG')
            #os.chdir('opencv-text-recognition')
            os.system('python text_recognition.py --east frozen_east_text_detection.pb')

    path2 = app.config['TEXT_OUT']+'/*.txt'
    files2 = glob.glob(path2)
    tex = []
    for texts in files2:
        with open(texts) as f:
            for line in f:
                # tex.append(line)
                line = line.strip('\n')
                line = line.strip('\t')
                line = line.strip(' ')
                line = line.strip('')
                tex.append(line)




    # for word in f.read().split():
    #     print(word)

    return render_template('upload.html', value=tex)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    app.run("0.0.0.0",5001,threaded=True,debug=True)
