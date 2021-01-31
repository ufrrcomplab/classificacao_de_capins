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
    
    # patch_image(filename,foldername,nRows,mCols)
    # Para encontrar o nRows e nCols basta dividir as dimensoes da imagem por 32.
    # Por exemplo: uma imagem de resolucao 5472x3648 teria 171 cols e 114 rows.
    patch_image(filename,foldername,34,47)

    # calculate_vi(foldername,npatches)
    # o npatches eh o numero de fragmentos da imagem, isto é, nrows*ncols=npatches.
    calculate_vi(foldername,1598)
    
    classify(foldername)

    # reconstruct_image(foldername,nrows,ncols,wid,hei)
    # mesmo valor de nRows e ncols do patch_image.py
    # hei e wid sao valores da resolucao da imagem.
    # exempo: 5472x3648, wid = 5472 e hei=3648.
    reconstruct_image(foldername,47,34,1504,1088)
    
    return send_from_directory('./images_classified/',foldername+'_classified.png', as_attachment=True)
    #return jsonify({"res":"done!"})
      
if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0',port=5000)