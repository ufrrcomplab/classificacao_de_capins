import pandas as pd
import pickle
import numpy as np
import os
import time
from flask import Flask, send_from_directory, request, flash, url_for, redirect, render_template, jsonify

#import scripts
from patch_image import *
from not_labeled_script import *
from model_script import *
from reconstruct_image import *

app = Flask(__name__)

UPLOAD_FOLDER = "./uploaded_images"


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
  return jsonify({"res":"working!"})

@app.route('/upload_image', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    file = request.files['image']
    foldername = str(int(time.time()))
    filename = foldername+".png"
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    patch_image(filename,foldername)
    calculate_vi(foldername)
    classify(foldername)
    reconstruct_image(foldername)
    
    return send_from_directory('./images_classified/',foldername+'_classified.png', as_attachment=True)
    #return jsonify({"res":"done!"})

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0', port=5000)