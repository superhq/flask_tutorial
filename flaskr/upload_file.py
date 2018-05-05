import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename

app = Flask(__name__)


@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        return 'OK'
    return render_template('upload_file.html')