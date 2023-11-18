import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import math
import os

def produce_models(genre, training_books, training_books_late, training_books_later, testing_books, testing_books_late, testing_books_later, average):
    if (len(training_books) < 30):
        print("There are not enough books in general.... this is bad... should not happen")
        with open('.' + os.sep + 'models'  + os.sep + genre + '-models.txt', 'w') as file:
            file.write("ERROR!!! NOT ENOUGH BOOKS FOUND FOR GENRE", genre)
        return
    #MODEL ON FULL DATE RANGE
    A = training_books['pub_date']
    A = np.array(A)
    #print(A)
    A = A.reshape(-1, 1)
    ones = [1] * len(A)
    ones = np.array(ones)
    ones = ones.reshape(-1, 1)
    A = np.concatenate((A, ones), axis=1)

    b = training_books['shelved'] / training_books['num_ratings']
    b = np.array(b)
    b = b.reshape(-1, 1)

    test_A = testing_books['pub_date']
    test_A = np.array(test_A)
    #print(A)
    test_A = test_A.reshape(-1, 1)
    ones = [1] * len(test_A)
    ones = np.array(ones)
    ones = ones.reshape(-1, 1)
    test_A = np.concatenate((test_A, ones), axis=1)

    b_test = testing_books['shelved'] / testing_books['num_ratings']
    b_test = np.array(b_test)
    b_test = b_test.reshape(-1, 1)

    regr = LinearRegression()
    regr.fit(A, b)
    ski_w1 = [regr.coef_, regr.intercept_]
    coef1 = ski_w1[0][0][0]
    intercept1 = ski_w1[1][0]
    MSE1 = MSE(test_A, b_test, ski_w1)[0][0]
    MAE1 = MAE(test_A, b_test, ski_w1)[0][0]
    print(f"{genre} model: y={coef1}x + {intercept1}")
    print("MSE: ", MSE1)
    print("MAE: ", MAE1)

    base_MSE = baseline_MSE(b_test, average)[0]
    base_MAE = baseline_MAE(b_test, average)[0]
    print(f"{genre} BASELINE model: y={average}x + 0")
    print("MSE: ", base_MSE)
    print("MAE: ", base_MAE)

    if (len(testing_books_late) < 30):
        print(f"The {genre} genre does not have enough books after 1940.")
    else:
        #MODEL ON BOOKS LATER THAN 1940 DATE RANGE
        A = training_books_late['pub_date']
        A = np.array(A)
        #print(A)
        A = A.reshape(-1, 1)
        ones = [1] * len(A)
        ones = np.array(ones)
        ones = ones.reshape(-1, 1)
        A = np.concatenate((A, ones), axis=1)

        b = training_books_late['shelved'] / training_books_late['num_ratings']
        b = np.array(b)
        b = b.reshape(-1, 1)

        test_A = testing_books_late['pub_date']
        test_A = np.array(test_A)
        #print(A)
        test_A = test_A.reshape(-1, 1)
        ones = [1] * len(test_A)
        ones = np.array(ones)
        ones = ones.reshape(-1, 1)
        test_A = np.concatenate((test_A, ones), axis=1)

        b_test = testing_books_late['shelved'] / testing_books_late['num_ratings']
        b_test = np.array(b_test)
        b_test = b_test.reshape(-1, 1)

        regr = LinearRegression()
        regr.fit(A, b)
        ski_w2 = [regr.coef_, regr.intercept_]
        coef2 = ski_w2[0][0][0]
        intercept2 = ski_w2[1][0]
        MSE2 = MSE(test_A, b_test, ski_w2)[0][0]
        MAE2 = MAE(test_A, b_test, ski_w2)[0][0]
        print(f"{genre} model2: y={coef2}x + {intercept2}")
        print("MSE: ", MSE2)
        print("MAE: ", MAE2)

    if (len(testing_books_later) < 30):
        print(f"The {genre} genre does not have enough books after 1990.")
    else:
        #MODEL ON BOOKS LATER THAN 1990 DATE RANGE
        A = training_books_later['pub_date']
        A = np.array(A)
        #print(A)
        A = A.reshape(-1, 1)
        ones = [1] * len(A)
        ones = np.array(ones)
        ones = ones.reshape(-1, 1)
        A = np.concatenate((A, ones), axis=1)

        b = training_books_later['shelved'] / training_books_later['num_ratings']
        b = np.array(b)
        b = b.reshape(-1, 1)

        test_A = testing_books_later['pub_date']
        test_A = np.array(test_A)
        #print(A)
        test_A = test_A.reshape(-1, 1)
        ones = [1] * len(test_A)
        ones = np.array(ones)
        ones = ones.reshape(-1, 1)
        test_A = np.concatenate((test_A, ones), axis=1)

        b_test = testing_books_later['shelved'] / testing_books_later['num_ratings']
        b_test = np.array(b_test)
        b_test = b_test.reshape(-1, 1)

        regr = LinearRegression()
        regr.fit(A, b)
        ski_w3 = [regr.coef_, regr.intercept_]
        coef3 = ski_w3[0][0][0]
        intercept3 = ski_w3[1][0]
        MSE3 = MSE(test_A, b_test, ski_w3)[0][0]
        MAE3 = MAE(test_A, b_test, ski_w3)[0][0]
        print(f"{genre} model3: y={coef3}x + {intercept3}")
        print("MSE: ", MSE3)
        print("MAE: ", MAE3)


    with open('.' + os.sep + 'models'  + os.sep + genre + '-models.txt', 'w') as file:
        file.write(f"{genre} models (first number is coefficient, second in intercept, third is MSE, last is MAE.)\n")
        file.write(f"baseline model: average shelved amount divided by average number of ratings:\n")
        file.write(f"{average}\n")
        file.write(f"0\n")
        file.write(f"{base_MSE}\n")
        file.write(f"{base_MAE}\n")
        file.write(f"model trained on all dates:\n")
        file.write(f"{coef1}\n")
        file.write(f"{intercept1}\n")
        file.write(f"{MSE1}\n")
        file.write(f"{MAE1}\n")
        if (len(testing_books_late) < 30):
            file.write(f"The {genre} genre does not have enough books after 1940.")
        else:
            file.write(f"model trained on dates after 1940:\n")
            file.write(f"{coef2}\n")
            file.write(f"{intercept2}\n")
            file.write(f"{MSE2}\n")
            file.write(f"{MAE2}\n")
        if (len(testing_books_later) < 30):
            file.write(f"The {genre} genre does not have enough books after 1990.")
        else:
            file.write(f"model trained on dates after 1990:\n")
            file.write(f"{coef3}\n")
            file.write(f"{intercept3}\n")
            file.write(f"{MSE3}\n")
            file.write(f"{MAE3}\n")
        
def MSE(A, b, w):
    sum = 0
    for i, y in enumerate(b):
        sum += (yPrime(w, A[i]) - y) ** 2
    return sum / len(b)

def baseline_MSE(b, baseline):
    sum = 0
    for i, y in enumerate(b):
        sum += (baseline - y) ** 2
    return sum / len(b)

def yPrime(w, x):
    return w[0]*x + w[1]

def MAE(A, b, w):
    sum = 0
    for i, y in enumerate(b):
        sum += abs(yPrime(w, A[i]) - y)
    return sum / len(b)

def baseline_MAE(b, baseline):
    sum = 0
    for i, y in enumerate(b):
        sum += abs(baseline - y)
    return sum / len(b)
