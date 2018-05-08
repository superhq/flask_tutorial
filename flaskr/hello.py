from flask import Flask,url_for,render_template,request,redirect,make_response,session,escape
from werkzeug.utils import secure_filename
import os


# class CustomFlask(Flask):
#     jinja_options = Flask.jinja_options.copy()
#     jinja_options.update(dict(
#         block_start_string='(%',
#         block_end_string='%)',
#         variable_start_string='((',
#         variable_end_string='))',
#         comment_start_string='(#',
#         comment_end_string='#)',
#     ))
#
#
# app = CustomFlask(__name__)

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'upload'
app.secret_key='123456'



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


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# Flask-Uploads ，这个扩展实现了一整套成熟的文件上传架构。它提供了包括文件类型白名单、黑名单等多种功能
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Each key in files is the name from the <input type="file" name="">
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(request.cookies.get('name'))
        return render_template('upload_file.html', filename=filename)
    resp = make_response(render_template('upload_file.html'))
    resp.set_cookie('name', 'hongqun')
    return resp


if __name__ == '__main__':
    app.debug = True
    app.run()