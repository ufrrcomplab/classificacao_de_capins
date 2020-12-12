import pickle
import pandas as pd
import csv

def classify(foldername):
    # load the model from disk
    model = 'svm_model_mpri.sav'
    loaded_model = pickle.load(open(model, 'rb'))
    filename = './csv_files/'+foldername+'.csv'
    save_path = './csv_classifications/'

    # load dataset
    df = pd.read_csv(filename, sep=',')
    #print(df['label'].value_counts())

    #get columns
    array = df.values
    X = array[:,:]
    #y = array[:,0]
    result = loaded_model.predict(X)

    pd.DataFrame(result).to_csv(save_path+foldername+"_labels.csv")
