import os
from wf_ml_evaluation import read_model
import matplotlib.pyplot as plt
import pandas as pd


import pickle

def predict(genre, avg):
    models = read_model(genre)

    dates_to_test = [1940, 1990, 2000, 2010, 2020, 2030]
    
    with open('.' + os.sep + 'prediction'  + os.sep + genre + '-predictions.txt', 'w') as file:
        print(f"\n{genre}:")
        file.write(f"\n {genre} average: {avg} ({avg * 1000 })\n")
        for i in range(3):
            print(f"Model {i+1} predictions:")
            file.write(f"Model {i+1} predictions:\n")
            for date in dates_to_test:
                if models[i] == None:
                    file.write(f"There wasn't enough books to train this model.")
                    continue
                if i == 1 and date < 1940:
                    file.write(f"{date}: This model wasn't tranied for this date.")
                    continue
                if (i == 2 and date < 1990):
                    file.write(f"{date}: This model wasn't tranied for this date.")
                    continue
                prediction = models[i][0]*date + models[i][1]
                print(f"{date}: {prediction} ({prediction * 1000})\n")
                file.write(f"{date}: {prediction} ({prediction * 1000})\n")
    if models[2] == None:
        return (genre, None)
    return (genre, models[2][0])

def import_processed_books(filename):
    with open(filename, 'rb') as infile:
        books = pickle.load(infile)
    return books

genres = []

with open('genres.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    if line[0] == '#' or line[0] == '\n':
        continue
    genres.append(line.replace('\n', ''))

coeffs = []
for genre in genres:
    path = '.'  + os.sep + 'data_processing'  + os.sep + '' + genre + '.pickle'
    books = import_processed_books(path)
    coeffs.append(predict(genre, books['shelved_avg'] / books['num_ratings_avg']))

coeffs = pd.DataFrame(coeffs)
coeffs = coeffs.sort_values(by=1, ascending=False)

print(coeffs)

fig, ax = plt.subplots()
ax.set(title='Model Coefficient Comparison', ylabel='Model Coefficient', xlabel='Genre')
ax.bar(coeffs[0], coeffs[1])
ax.bar(coeffs[0], coeffs[2])
fig.set_figwidth(150)
fig.set_figheight(10)
plt.savefig('.'  + os.sep + 'evaluation'  + os.sep + '_ModelCoefficientComparison.png')

coeffs = coeffs[coeffs[0] != 'cosmere']

fig, ax = plt.subplots()
ax.set(title='Model Coefficient Comparison', ylabel='Model Coefficient', xlabel='Genre')
ax.bar(coeffs[0], coeffs[1])
fig.set_figwidth(150)
fig.set_figheight(10)
plt.savefig('.'  + os.sep + 'evaluation'  + os.sep + '_ModelCoefficientComparison(No Cosmere).png')