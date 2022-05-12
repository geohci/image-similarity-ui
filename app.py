import os
import yaml

from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)

VALID_IMAGE_EXTENSIONS = ['.jpg', '.png', '.svg', '.gif', '.jpeg', '.tif', '.bmp', '.webp', '.xcf']

__dir__ = os.path.dirname(__file__)
app.config.update(
    yaml.safe_load(open(os.path.join(__dir__, 'default_config.yaml'))))
try:
    app.config.update(
        yaml.safe_load(open(os.path.join(__dir__, 'config.yaml'))))
except IOError:
    # It is ok if there is no local config file
    pass

# Enable CORS for API endpoints
#CORS(app, resources={'*': {'origins': '*'}})
CORS(app)

@app.route('/')
def index():
    image_name = validate_api_args()
    return render_template('index.html', image_name=image_name)

def valildate_commons_image(image_name):
    # ex: File:YellowCreek.jpg
    if image_name.startswith("File:"):
        image_name = image_name[5:]
    # ex: http://upload.wikimedia.org/wikipedia/commons/9/93/YellowCreek.jpg
    elif 'upload.wikimedia.org/wikipedia/commons' in image_name:
        image_name = image_name.split('/')[-1]
    # ex: https://commons.wikimedia.org/wiki/File:Nuselsky-most.jpg
    elif 'commons.wkimedia.org/wiki/File:' in image_name:
        image_name = image_name.split('/wiki/')[-1][5:]

    for img_ext in VALID_IMAGE_EXTENSIONS:
        if image_name.lower().endswith(img_ext):
            return image_name
    return None

def validate_api_args():
    image_name = valildate_commons_image(request.args.get('image_name', ''))
    return image_name