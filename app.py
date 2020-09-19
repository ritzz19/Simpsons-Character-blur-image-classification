#Usage: python app.py
import os
 
from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import numpy as np
import argparse
import imutils
import cv2
import time
import uuid
from PIL import Image


from tensorflow.keras import layers
import base64
import tensorflow as tf
img_width, img_height = 224, 224
model_path = './models/VGG16_res_final.h5'
#model_weights_path = './models/weights.h5'

#model = load_model(model_path)
model = tf.keras.models.load_model(model_path,custom_objects={'AttentionLayer': layers.Conv1D})

folderList = ['0. apu_nahasapeemapetilon', '1. barney_gumble','2. bart_simpson','3. charles_montgomery_burns','4. homer_simpson','5. lisa_simpson',
              '6. marge_simpson','7. maggie_simpson','8. ned_flanders','9. krusty_the_clown']


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg','png'])

def get_as_base64(url):
    return base64.b64encode(request.get(url).content)

def predict(file):

    x = load_img(file, target_size=(img_width,img_height))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = model.predict(x)
    result = array[0]
    answer = np.argmax(result)
    if answer == 0:
        print("Label: 0")
    elif answer == 1:
	    print("Label: 1")
    elif answer == 2:
	    print("Label: 2")
    elif answer == 3:
        print("Label: 3")
    elif answer == 4:
        print("Label: 4")
    elif answer == 5:
        print("Label: 5")
    elif answer == 6:
        print("Label: 6")
    elif answer == 7:
        print("Label: 7")
    elif answer == 8:
        print("Label: 8")
    elif answer == 9:
        print("Label: 9")
    return answer

def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def template_test():
    return render_template('template.html', label='', imagesource='../uploads/test.png')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        import time
        start_time = time.time()
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            result = predict(file_path)
            label = folderList[result]
            print(result)
            print(file_path)
            filename = my_random_string(6) + filename

            os.rename(file_path, os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("--- %s seconds ---" % str (time.time() - start_time))
            return render_template('template.html', label=label, imagesource='../uploads/' + filename)

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

from werkzeug import SharedDataMiddleware
app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})

if __name__ == "__main__":
    app.debug=False
    app.run(debug=True)
