import pickle
import pandas as pd
import matplotlib.pyplot as plt
import os

def import_processed_books(filename):
    with open(filename, 'rb') as infile:
        books = pickle.load(infile)
    return books

def compute_stats(books, genre):
    df = pd.DataFrame.from_dict(books['books'], orient='index')
    df = df.drop('title', axis=1)
    df = df.drop('author', axis=1)
    med = df.median()
    
    with open('.' + os.sep + 'data_processing'  + os.sep + genre + '-summary.txt', 'w') as file:
        file.write('==========================\n')
        file.write(genre + '\n')
        file.write('==========================\n')

        file.write('\nNumber of times the books have been shelved in that genre shelf\n')
        file.write('avg:' +  str(books['shelved_avg']) + '\n')
        file.write('min:'+ str(books['shelved_min']) + '\n')
        file.write('max:'+ str(books['shelved_max']) + '\n')
        file.write('median:' + str(med['shelved']) + '\n')

        file.write('\nRating\n')
        file.write('avg:'+ str(books['rating_avg']) + '\n')
        file.write('min:'+ str(books['rating_min']) + '\n')
        file.write('max:'+ str(books['rating_max']) + '\n')
        file.write('median:' + str(med['rating']) + '\n')

        file.write('\nPublication Date\n')
        file.write('avg:'+ str(books['pub_date_avg']) + '\n')
        file.write('min:'+ str(books['pub_date_min']) + '\n')
        file.write('max:'+ str(books['pub_date_max']) + '\n')
        file.write('median:' + str(med['pub_date']) + '\n')

        file.write('\nNumber of Ratings\n')
        file.write('avg:'+ str(books['num_ratings_avg']) + '\n')
        file.write('min:'+ str(books['num_ratings_min']) + '\n')
        file.write('max:'+ str(books['num_ratings_max']) + '\n')
        file.write('median:' + str(med['num_ratings']) + '\n')

        file.write('\nSeries\n')
        file.write('There are two categories here: In a Series or Not in a Series\n')
        file.write('I just have the percentage here since most and least frequent are trivial to understand from this :)\n')
        file.write('Percent of books in series: '+ str(books['series_num'] / books['count'] * 100) + '%\n')
        file.write('\n')

    #, columns=['rating', 'pub_date', 'shelved', 'num_ratings']
    print(df)
    with open('.'  + os.sep + 'visuals'  + os.sep + 'CorrelationMatrices'  + os.sep + genre + '-matrix.txt', 'w') as file:
        file.write(df.corr().to_string())
    print(df.corr())

    #AB - rating to publicagtion date
    fig, ax = plt.subplots()
    ax.set(title='Rating to Publication Date: ' + genre, ylabel='Rating', xlabel='Publication Date')
    plt.scatter(df['pub_date'], df['rating'])
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'RatingToPubDate'  + os.sep + 'RatingToPubDate' + genre +'.png')

    #AC - rating to shelved
    fig, ax = plt.subplots()
    ax.set(title='Rating to Shelved Amount: ' + genre, ylabel='Rating', xlabel='Shelved Amount')
    plt.scatter(df['shelved'], df['rating'])
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'RatingToShelved'  + os.sep + 'RatingToShelved' + genre +'.png')

    #AD - rating to num ratings
    fig, ax = plt.subplots()
    ax.set(title='Rating to Number of Ratings: ' + genre, ylabel='Rating', xlabel='Number of Ratings')
    plt.scatter(df['num_ratings'], df['rating'])
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'RatingToNumRatings'  + os.sep + 'RatingToNumRatings' + genre +'.png')

    #BC - pub date to shelved 
    fig, ax = plt.subplots()
    ax.set(title='Shelved Amount to Publication Date: ' + genre, ylabel='Shelved', xlabel='Publication Date')
    plt.scatter(df['pub_date'], df['shelved'])
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'ShelvedToPubDate'  + os.sep + 'ShelvedToPubDate' + genre +'.png')

    #BD - pub date to num ratings
    fig, ax = plt.subplots()
    ax.set(title='Number of Ratings to Publication Date: ' + genre, ylabel='Number of Ratings', xlabel='Publication Date')
    plt.scatter(df['pub_date'], df['num_ratings'])
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'NumRatingsToPubDate'  + os.sep + 'NumRatingsToPubDate' + genre +'.png')

    #CD - shelved to num ratings
    fig, ax = plt.subplots()
    ax.set(title='Shelved Amount to Number of Ratings: ' + genre, ylabel='Shelved Amount', xlabel='Number of Ratings')
    plt.scatter(df['num_ratings'], df['shelved'])
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'ShelvedToNumRatings'  + os.sep + 'ShelvedToNumRatings' + genre +'.png')

    #ShelvedRatingsRationByPubDate
    fig, ax = plt.subplots()
    ax.set(title='Shelved Amount to Number of Ratings By Publication Date: ' + genre, ylabel='Shelved-Ratings Ratio', xlabel='Publication Date')
    plt.scatter(df['pub_date'], df['num_ratings'] / df['shelved'] )
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'ShelvedRatingsRatioByPubDate'  + os.sep + 'ShelvedRatingsRatioByPubDate' + genre +'.png')

    #series or no series
    fig, ax = plt.subplots()
    ax.set(title='Is a particular book in a series: ' + genre, ylabel='Number of Books', xlabel='In Series?')
    plt.hist(df['series'].astype(str), bins=2)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'Series'  + os.sep + 'Series' + genre +'.png')

    fig, ax = plt.subplots()
    ax.set(title='Is a particular book in a series: ' + genre, ylabel='Number of Books', xlabel='In Series?')
    ax.pie([books['series_num'] / books['count'] * 100, 100 - books['series_num'] / books['count'] * 100], labels=['Series', 'Not In Series'])
    ax.axis('equal')
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'Series'  + os.sep + 'SeriesPie' + genre +'.png')

def compare_genres(books):
    df = pd.DataFrame.from_dict(books, orient='index')
    #df = df.drop('books')
    #print(df)
    #print(df.corr(numeric_only=True))

    #str = df[genre]['num_ratings_avg'] * df[genre]['shelved_avg']
    strs = df['num_ratings_avg'] * df['shelved_avg']

    fig, ax = plt.subplots()
    ax.set(title='Genre Strength (Average Shelved Amount * Average Number of Reviews)', ylabel='Strength', xlabel='Genre')
    ax.bar(strs.index, strs)
    fig.set_figwidth(150)
    fig.set_figheight(10)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'GenreStrengthComparison.png')

    strs = strs.sort_values(ascending=False)

    fig, ax = plt.subplots()
    ax.set(title='Genre Strength (Average Shelved Amount * Average Number of Reviews)', ylabel='Strength', xlabel='Genre')
    ax.bar(strs.index, strs)
    fig.set_figwidth(150)
    fig.set_figheight(10)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'GenreStrengthComparisonSorted.png')

    fig, ax = plt.subplots()
    ax.set(title='Shelved Comparison', ylabel='Shelved Amount', xlabel='Genre')
    ax.bar(df.index, df['shelved_avg'])
    fig.set_figwidth(150)
    fig.set_figheight(10)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'ShelvedComparison.png')

    shelved_comp = df['shelved_avg']
    shelved_comp = shelved_comp.sort_values(ascending=False)
    fig, ax = plt.subplots()
    ax.set(title='Shelved Comparison', ylabel='Shelved Amount', xlabel='Genre')
    ax.bar(shelved_comp.index, shelved_comp)
    fig.set_figwidth(150)
    fig.set_figheight(10)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'ShelvedComparisonSorted.png')

    fig, ax = plt.subplots()
    ax.set(title='Shelved to Number of Ratings Ratio Comparison', ylabel='Shelved to Number of Ratings Ratio', xlabel='Genre')
    ax.bar(df.index, df['shelved_avg'] / df['num_ratings_avg'])
    fig.set_figwidth(150)
    fig.set_figheight(10)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'ShelvedRatingsRatioComparison.png')

    ratio = df['shelved_avg'] / df['num_ratings_avg']
    ratio = ratio.sort_values(ascending=False)
    fig, ax = plt.subplots()
    ax.set(title='Shelved to Number of Ratings Ratio Comparison', ylabel='Shelved to Number of Ratings Ratio', xlabel='Genre')
    ax.bar(ratio.index, ratio)
    fig.set_figwidth(150)
    fig.set_figheight(10)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'ShelvedRatingsRatioComparisonSorted.png')

    ratio = df['shelved_avg'] / df['num_ratings_avg']
    ratio *= 1000
    ratio = ratio.sort_values(ascending=False)
    fig, ax = plt.subplots()
    ax.set(title='Shelved to Number of Ratings Ratio Comparison', ylabel='Shelved to Number of Ratings Ratio', xlabel='Genre')
    ax.bar(ratio.index, ratio)
    fig.set_figwidth(150)
    fig.set_figheight(10)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'ShelvedRatingsRatio1000ComparisonSorted.png')

    ratio = df['shelved_avg'] / df['num_ratings_avg']
    ratio *= 1000
    fig, ax = plt.subplots()
    ax.set(title='Shelved to Number of Ratings Ratio Comparison', ylabel='Shelved to Number of Ratings Ratio', xlabel='Genre')
    ax.bar(ratio.index, ratio)
    fig.set_figwidth(150)
    fig.set_figheight(10)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'ShelvedRatingsRatio1000Comparison.png')

    num_ratings = df['num_ratings_avg']
    fig, ax = plt.subplots()
    ax.set(title='Number of Ratings Comparison', ylabel='Number of Ratings', xlabel='Genre')
    ax.bar(num_ratings.index, num_ratings)
    fig.set_figwidth(150)
    fig.set_figheight(10)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'NumberOfRatingsComparison.png')

    num_ratings = num_ratings.sort_values(ascending=False)
    fig, ax = plt.subplots()
    ax.set(title='Number of Ratings Comparison (Sorted)', ylabel='Number of Ratings', xlabel='Genre')
    ax.bar(num_ratings.index, num_ratings)
    fig.set_figwidth(150)
    fig.set_figheight(10)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'NumberOfRatingsComparisonSorted.png')

    pub_date = df['pub_date_avg'] - 1950
    fig, ax = plt.subplots()
    ax.set(title='Publication Date - Years from 1950 - Comparison', ylabel='Publication Date', xlabel='Genre')
    ax.bar(pub_date.index, pub_date)
    fig.set_figwidth(150)
    fig.set_figheight(10)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'PublicationDate-YearsFrom1950-Comparison.png')

    pub_date = pub_date.sort_values(ascending=False)
    fig, ax = plt.subplots()
    ax.set(title='Publication Date - Years from 1950 - Comparison (Sorted)', ylabel='Publication Date', xlabel='Genre')
    ax.bar(pub_date.index, pub_date)
    fig.set_figwidth(150)
    fig.set_figheight(10)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'PublicationDate-YearsFrom1950-ComparisonSorted.png')

    series = (df['series_num'] / df['count']) *100
    fig, ax = plt.subplots()
    ax.set(title='Percent of Books in Series Comparison', ylabel='Percent of Books in Series', xlabel='Genre')
    ax.bar(series.index, series)
    fig.set_figwidth(150)
    fig.set_figheight(10)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'SeriesComparison.png')

    series = series.sort_values(ascending=False)
    fig, ax = plt.subplots()
    ax.set(title='Percent of Books in Series Comparison (Sorted)', ylabel='Percent of Books in Series', xlabel='Genre')
    ax.bar(series.index, series)
    fig.set_figwidth(150)
    fig.set_figheight(10)
    plt.savefig('.'  + os.sep + 'visuals'  + os.sep + 'SeriesComparisonSorted.png')

def visualize(genres):
    all_genres = {}

    for genre in genres:
        path = '.'  + os.sep + 'data_processing'  + os.sep + '' + genre + '.pickle'
        books = import_processed_books(path)
        all_genres[genre] = books
        compute_stats(books, genre)

    compare_genres(all_genres)

genres = []

with open('genres.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    if line[0] == '#' or line[0] == '\n':
        continue
    genres.append(line.replace('\n', ''))

all_genres = {}

for genre in genres:
    path = '.'  + os.sep + 'data_processing'  + os.sep + '' + genre + '.pickle'
    books = import_processed_books(path)
    all_genres[genre] = books
    #compute_stats(books, genre)

compare_genres(all_genres)