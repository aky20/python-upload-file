from flask import Flask, redirect, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        app.config['UPLOAD_FOLDER'] = "./static/img/uploads/"
        image = request.files['image']
        if allowed_file(image.filename):
            image.save(app.config['UPLOAD_FOLDER'] + "profile.png")

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
