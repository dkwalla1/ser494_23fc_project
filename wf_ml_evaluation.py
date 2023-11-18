import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.utils import shuffle 
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import math
from wf_ml_training import produce_models
from wf_ml_training import MSE
from wf_ml_training import MAE


def import_processed_books(filename):
    with open(filename, 'rb') as infile:
        books = pickle.load(infile)
    return books

def split_all_data(genres):
    all_genres = {}
    models = []

    for genre in genres:
        path = '.'  + os.sep + 'data_processing'  + os.sep + '' + genre + '.pickle'
        books = import_processed_books(path)
        all_genres[genre] = books
        split_data_and_produce_models(books, genre)    

def split_data_and_produce_models(books, genre):
    RERUN_OVERALL_SUMMARY = False #you have to delete the current values in _overall-summary since it will just append to it before changing this to True
    FRACTION_TRAINING = 0.8
    average = books['shelved_avg'] / books['num_ratings_avg']

    books = pd.DataFrame.from_dict(books['books'], orient="index")
    books = books[['pub_date', 'shelved', 'num_ratings']]
    books = books.dropna(how='any')
    

    training_books = []
    training_books_late = []
    training_books_later = []
    testing_books = []
    testing_books_late = []
    testing_books_later = []
    count = 0
    while count < 50:
        count += 1
        shuffled_books = shuffle(books)
        shuffled_books = shuffled_books.apply(pd.to_numeric)

        split = int(len(shuffled_books) * FRACTION_TRAINING)   
        training_books = shuffled_books[:split]
        testing_books = shuffled_books[split:]
        if (len(testing_books) < 30):
            continue

        late_books = shuffled_books[(shuffled_books['pub_date'] > 1940)]
        split = int(len(late_books) * FRACTION_TRAINING)
        training_books_late = late_books[:split]
        testing_books_late = late_books[split:]
        if (len(testing_books_late) < 30):
            continue

        later_books = shuffled_books[(shuffled_books['pub_date'] > 1990)]
        split = int(len(later_books) * FRACTION_TRAINING)
        training_books_later = later_books[:split]
        testing_books_later = later_books[split:]
        if len(testing_books_later) < 30:
            continue

        break
    if count >= 50:
        print(f"\n\n\n\nThe {genre} genre has too few books for all models to be produced")
        print(training_books, len(training_books))

    produce_models(genre, training_books, training_books_late, training_books_later, testing_books, testing_books_late, testing_books_later, average)
    
    models = read_model(genre)
    with open('.' + os.sep + 'evaluation'  + os.sep + genre + '-summary.txt', 'w') as file:
        file.write(f"Mean Squared Error and Mean Absolute Error for {genre} genre.\n")
        for m, model in enumerate(models):
            if model == None:
                continue
            file.write(f"Model {m}:\n")

            file.write("Testing MSE:\n")
            file.write(f"{model[2]}\n")
            file.write("Testing MAE:\n")
            file.write(f"{model[3]}\n\n")

    if (RERUN_OVERALL_SUMMARY):
        with open('.' + os.sep + 'evaluation'  + os.sep +  '_overall-summary.txt', 'a') as file:
            if models[2] == None:
                file.write(f"{genre}: No 3rd Model\n")
            elif (models[2][0] > 0):
                file.write(f"{genre}: Positive\n")
            else:
                file.write(f"{genre}: Negative\n")
            

def read_model(genre):
    with open('.' + os.sep + 'models'  + os.sep + genre + '-models.txt', 'r') as file:
        lines = file.readlines()

    coef_base = float(lines[2].replace('\n', ''))
    intercept_base = float(lines[3].replace('\n', ''))
    MSE_base = float(lines[4].replace('\n', ''))
    MAE_base = float(lines[5].replace('\n', ''))

    coef1 = float(lines[7].replace('\n', ''))
    intercept1 = float(lines[8].replace('\n', ''))
    MSE1 = float(lines[9].replace('\n', ''))
    MAE1 = float(lines[10].replace('\n', ''))
    # print(coef1)
    # print(intercept1)
    # print(MSE1)
    # print(MAE1)

    #Doesn't read the data if there wasn't enough books to produce it
    if (lines[11].startswith('T')):
        return [(coef_base, intercept_base, MSE_base, MAE_base), (coef1, intercept1, MSE1, MAE1), None, None]
    coef2 = float(lines[12].replace('\n', ''))
    intercept2 = float(lines[13].replace('\n', ''))
    MSE2 = float(lines[14].replace('\n', ''))
    MAE2 = float(lines[15].replace('\n', ''))
    # print(coef2)
    # print(intercept2)
    # print(MSE2)
    # print(MAE2)

    #Doesn't read the data if there wasn't enough books to produce it
    if (lines[16].startswith('T')):
        return [(coef_base, intercept_base, MSE_base, MAE_base), (coef1, intercept1, MSE1, MAE1), (coef2, intercept2, MSE2, MAE2), None]
    coef3 = float(lines[17].replace('\n', ''))
    intercept3 = float(lines[18].replace('\n', ''))
    MSE3 = float(lines[19].replace('\n', ''))
    MAE3 = float(lines[20].replace('\n', ''))
    # print(coef3)
    # print(intercept3)
    # print(MSE3)
    # print(MAE3)

    return [(coef_base, intercept_base, MSE_base, MAE_base), (coef1, intercept1, MSE1, MAE1), (coef2, intercept2, MSE2, MAE2), (coef3, intercept3, MSE3, MAE3)]

genres = []

with open('genres.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    if line[0] == '#' or line[0] == '\n':
        continue
    genres.append(line.replace('\n', ''))

split_all_data(genres)