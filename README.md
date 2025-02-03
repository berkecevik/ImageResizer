# Image Resizer Web App  

This is a simple Flask-based web application that allows users to upload multiple images and automatically resizes them to 300x300 pixels. The resized images maintain their aspect ratio and are centered on a 300x300 canvas.  

## Features  
- Upload multiple images at once  
- Automatically resizes images to 300x300 pixels  
- Maintains aspect ratio and centers images on a white background  
- Download resized images  

## Installation  

### Prerequisites  
Ensure you have the following installed:  
- Python 3.x  
- pip (Python package manager)  

### Clone the Repository  
```bash
git clone https://github.com/berkecevik/ImageResizer.git
cd your-repository
```

### Install Dependencies  
```bash
pip install -r requirements.txt
```

## Usage  

1. Run the Flask application:  
   ```bash
   python resizer.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000/`  
3. Upload images through the web interface  
4. The resized images will be saved in the `RESIZED_FOLDER`  
5. Download resized images when needed  

## Folder Structure  
```
your-repository/
│── uploads/           # Temporary folder for uploaded images  
│── resizer.py         # Main Flask application  
│── templates/         # HTML templates  
│── requirements.txt   # Python dependencies  
│── README.md          # Documentation  
```

## Configuration  
By default, resized images are stored in:  
```python
RESIZED_FOLDER = r'C:\Users\YourFile'
```
You can change this path in `resizer.py` to suit your needs.  

## Dependencies  
This project requires the following Python packages:  
- Flask  
- Pillow  

You can install them using:  
```bash
pip install Flask Pillow
```

## License  
This project is open-source and available under the MIT License.

