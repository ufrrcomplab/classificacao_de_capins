import csv
import cv2
import numpy as np

def calculate_vi(foldername,npatches):
    #Create csv file
    dir_name = "./patched_images/"+foldername
    cols = ['pixel0']
    qt_pixels = 32*32
    filename = "./csv_files/"+foldername+".csv"

    for i in range(1,qt_pixels):
        p = 'pixel'+str(i)
        cols.append(p)

    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(cols)

    #Vegetation index 
    for k in range(1,npatches+1):
        #abrir imagem
        image = cv2.imread(dir_name+'/patch_'+str(k)+'.jpg')
        
        ### SEPARACAO DAS BANDAS DE CORES ###
        
        #extrair as cores da imagem bgr
        channel_blue = image[:,:,0]
        channel_green = image[:,:,1]
        channel_red = image[:,:,2]

        #transformar a numpy.array
        blue_arr = np.array(channel_blue,dtype=np.float32)
        green_arr = np.array(channel_green,dtype=np.float32)
        red_arr = np.array(channel_red,dtype=np.float32)
    
        #normalizar as bandas RGB dividindo por 255
        normal_channel_blue = channel_blue/255
        normal_channel_green = channel_green/255
        normal_channel_red = channel_red/255

        #calcular as coordenadas cromáticas de cada banda espectral
        #para calcular isso devemos dividir toda a banda pelo maior valor dentro dela
        crom_blue = normal_channel_blue/np.max(normal_channel_blue)
        crom_green = normal_channel_green/np.max(normal_channel_green)
        crom_red = normal_channel_red/np.max(normal_channel_red)

        #Calculando o índice ExR
        exr = (1.4*crom_red - crom_green)
        #Calculando o índice ExG
        exg = (2*crom_green - crom_red - crom_blue)
        
        #Calculando o índice ExGR
        exgr = exg - exr
        

        ### SALVAR RESULTADO DO INDICE NO ARQUIVO CSV ###
        
        values = list(exgr.flatten()) #not labeled
        
        #SALVA OS values QUE SAO 32 X 32 A IMAGEM
        if (len(values) == 1024):
            with open(filename, 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',')
                spamwriter.writerow(values)
