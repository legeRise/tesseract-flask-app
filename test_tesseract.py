from flask import Flask, request, render_template_string
from PIL import Image
import pytesseract

app = Flask(__name__)

# Ensure the Tesseract-OCR executable is in your PATH
# If not, you might need to specify the path to the executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows example

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            image = Image.open(file.stream)
            text = pytesseract.image_to_string(image)
            return render_template_string('''
                <h1>Extracted Text</h1>
                <pre>{{ text }}</pre>
                <a href="/">Go Back</a>
            ''', text=text)
    return '''
        <!doctype html>
        <title>Upload an Image</title>
        <h1>Upload an Image for OCR</h1>
        <form action="/" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
