from flask import Flask, request, render_template, send_from_directory
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
RESIZED_FOLDER = r'C:\Users\YourFile'

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESIZED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files[]' not in request.files:
        return 'No files part'
    files = request.files.getlist('files[]')

    for file in files:
        if file.filename == '':
            return 'No selected file'
        image = Image.open(file).convert("RGBA")  # Ensure image is in RGBA mode
        
        # Maintain aspect ratio and resize
        image.thumbnail((300, 300))
        
        # Create a new white (or transparent) 300x300 canvas
        new_image = Image.new("RGBA", (300, 300), (255, 255, 255, 255))
        
        # Center the resized image on the new canvas
        x_offset = (300 - image.width) // 2
        y_offset = (300 - image.height) // 2
        
        # Paste image without transparency issues
        new_image.paste(image, (x_offset, y_offset), mask=image if image.mode == 'RGBA' else None)
        
        # Save the fixed image
        new_image.convert("RGB").save(os.path.join(RESIZED_FOLDER, file.filename), format="PNG")

    return 'Files uploaded and resized successfully!'

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(RESIZED_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
