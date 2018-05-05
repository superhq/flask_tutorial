from flask import Flask,url_for,render_template,request,redirect
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'upload'

@app.route('/')
def hello():
    return 'Hello, My World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/url/<name>')
def url(name):
    return url_for(name)

@app.route('/index/<name>')
@app.route('/index')
def index(name=None):
    return  render_template('index.html',name=name)


@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return render_template('upload_file.html',filename=filename)
    return render_template('upload_file.html')


if __name__ == '__main__':
    app.debug = True
    app.run()