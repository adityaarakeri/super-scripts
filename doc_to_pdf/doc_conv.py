from flask import Flask,abort,render_template,request,redirect,url_for,send_file,after_this_request
from werkzeug import secure_filename
from glob import glob
import sys
import os
#from pythoncom import CoUninitialize
import comtypes.client
import os
app = Flask(__name__)
UPLOAD_FOLDER = os.getcwd()+'\\uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
@app.route('/')
def index():
    return redirect(url_for('upload_file'))
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('upload_comp.html',name=name)

@app.route('/upload/',methods = ['GET','POST'])
def upload_file():
    if request.method =='POST':
        file = request.files['file[]']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return return_file()
    return render_template('Upload.html')
@app.route('/return-files', methods=['GET'])
def return_file():
  #  os.system("conda activate aryu_dev")
    os.system("python conv.py")
    os.system('python del_file.py')
    return send_file(UPLOAD_FOLDER+"\\Converted.pdf", as_attachment=True)
if __name__ == '__main__':
    app.run(debug = True)