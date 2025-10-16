from flask import Flask, render_template, request, redirect, url_for
from ocr import ocr_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect('/')
    
    image = request.files['image']

    if image.filename == '':
        return redirect('/')

    if image:
        image_path = f"{app.config['UPLOAD_FOLDER']}/{image.filename}"
        image.save(image_path)
        result = ocr_image(image_path)
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
