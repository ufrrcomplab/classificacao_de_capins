import cv2
import sys
import os

def patch_image(filename,foldername,nRows,mCols):
    dirName = "./patched_images/"+foldername
    if not os.path.exists(dirName):
        os.makedirs(dirName)

    # O numero de colunas e linhas eh relativo a resolucao da image.
    # Para encontrar o nRows e nCols basta dividir as dimensoes da imagem por 32.
    # Por exemplo: uma imagem de resolucao 5472x3648 teria 171 cols e 114 rows.
    #nRows = 34
    # Number of columns
    #mCols = 47
    # Starting counter
    count = 0

    
    # Reading image
    img = cv2.imread('./uploaded_images/'+filename)

    #cv2.imshow('image',img)

    # Dimensions of the image
    sizeX = img.shape[1]
    sizeY = img.shape[0]

    #print(img.shape)

    for i in range(0,nRows):
        for j in range(0, mCols):
            a=int(i*sizeY/nRows)
            b=int(i*sizeY/nRows + sizeY/nRows)
            c=int(j*sizeX/mCols)
            d=int(j*sizeX/mCols + sizeX/mCols)
            #print(a," ",b," ",c," ",d)
            roi = img[a:b,c:d]
            #cv2.imshow('rois'+str(i)+str(j), roi)
            count += 1
            cv2.imwrite(dirName+'/patch_'+str(count)+".jpg", roi)
