import numpy as np
import PIL
from PIL import Image, ImageDraw
import pandas as pd

def reconstruct_image(foldername,nrows,ncols,wid,hei):
    dir_name = './patched_images/'+foldername
    labels_file = './csv_classifications/'+foldername+'_labels.csv'
    save_path = './images_classified/'

    df = pd.read_csv(labels_file, sep=',')
    labels = df.values
    start_row = 0
    # mesmo valor de nRows do patch_image.py
    end_row = nrows
    increment = end_row

    reso = 32*wid

    for j in range (1,ncols+1):
        list_im = [dir_name+'/patch_'+str(i)+'.jpg' for i in range(start_row+1,end_row+1)]
        c = 0 #contador para iterar no array de imagens

        imgs    = [ PIL.Image.open(i) for i in list_im ]

        for k in range(start_row,end_row):
            if(labels[k][1] == 100): #se infestado fazer as bordas vermelhas na imagem
                infested = ImageDraw.Draw(imgs[c])   
                infested.rectangle([(0,0),(31,31)], fill = None, outline ="red") 
                #imgs[k].save("infested.jpg")
                c += 1

        start_row = end_row
        end_row += increment
        
        img_row = np.hstack(imgs)

        if(j == 1):
            imgs_comb = np.vstack(img_row)
        else:
            imgs_comb = np.vstack((imgs_comb, img_row.reshape(reso,3)))

        del img_row #liberar img_row

        j += increment

    # save the picture
    imgs_comb = PIL.Image.fromarray(imgs_comb.reshape(hei,wid,3))
    imgs_comb.save(save_path+foldername+'_classified.png')    

