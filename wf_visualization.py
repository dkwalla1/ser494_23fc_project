import pickle
import pandas as pd
import matplotlib.pyplot as plt

def import_processed_books(filename):
    with open(filename, 'rb') as infile:
        books = pickle.load(infile)
    return books

def compute_stats(books, genre):

    print('==========================')
    print(genre)
    print('==========================')

    print('shelved')
    print('avg', books['shelved_avg'])
    print('min', books['shelved_min'])
    print('max', books['shelved_max'])

    print('\nrating')
    print('avg', books['rating_avg'])
    print('min', books['rating_min'])
    print('max', books['rating_max'])

    print('\npub date')
    print('avg', books['pub_date_avg'])
    print('min', books['pub_date_min'])
    print('max', books['pub_date_max'])

    print('\nnum ratings')
    print('avg', books['num_ratings_avg'])
    print('min', books['num_ratings_min'])
    print('max', books['num_ratings_max'])

    print('\nseries')
    print('categories: 2')
    print('percent in series: ', books['series_num'] / books['count'] * 100, '%')
    print('')
    #, columns=['rating', 'pub_date', 'shelved', 'num_ratings']
    df = pd.DataFrame.from_dict(books['books'], orient='index')
    df = df.drop('title', axis=1)
    df = df.drop('author', axis=1)
    print(df.median())
    print(df)
    print(df.corr())

    #AB - rating to publicagtion date
    fig, ax = plt.subplots()
    ax.set(title='Rating to Publication Date: ' + genre, ylabel='Rating', xlabel='Publication Date')
    plt.scatter(df['pub_date'], df['rating'])
    plt.savefig('./visuals/RatingToPubDate/RatingToPubDate' + genre +'.png')

    #AC - rating to shelved
    fig, ax = plt.subplots()
    ax.set(title='Rating to Shelved Amount: ' + genre, ylabel='Rating', xlabel='Shelved Amount')
    plt.scatter(df['shelved'], df['rating'])
    plt.savefig('./visuals/RatingToShelved/RatingToShelved' + genre +'.png')

    #AD - rating to num ratings
    fig, ax = plt.subplots()
    ax.set(title='Rating to Number of Ratings: ' + genre, ylabel='Rating', xlabel='Number of Ratings')
    plt.scatter(df['num_ratings'], df['rating'])
    plt.savefig('./visuals/RatingToNumRatings/RatingToNumRatings' + genre +'.png')

    #BC - pub date to shelved 
    fig, ax = plt.subplots()
    ax.set(title='Shelved Amount to Publication Date: ' + genre, ylabel='Shelved', xlabel='Publication Date')
    plt.scatter(df['pub_date'], df['shelved'])
    plt.savefig('./visuals/ShelvedToPubDate/ShelvedToPubDate' + genre +'.png')

    #BD - pub date to num ratings
    fig, ax = plt.subplots()
    ax.set(title='Number of Ratings to Publication Date: ' + genre, ylabel='Number of Ratings', xlabel='Publication Date')
    plt.scatter(df['pub_date'], df['num_ratings'])
    plt.savefig('./visuals/NumRatingsToPubDate/NumRatingsToPubDate' + genre +'.png')

    #CD - shelved to num ratings
    fig, ax = plt.subplots()
    ax.set(title='Shelved Amount to Number of Ratings: ' + genre, ylabel='Shelved Amount', xlabel='Number of Ratings')
    plt.scatter(df['num_ratings'], df['shelved'])
    plt.savefig('./visuals/ShelvedToNumRatings/ShelvedToNumRatings' + genre +'.png')

    #series or no series
    fig, ax = plt.subplots()
    ax.set(title='Is a particular book in a series: ' + genre, ylabel='Number of Books', xlabel='In Series?')
    plt.hist(df['series'], bins=2)
    plt.savefig('./visuals/Series/Series' + genre +'.png')


high_genres = ['fiction', 'non-fiction', 'romance', 'historical', 'fantasy', 'scifi', 'classics', 'mystery', 'thriller', 'young-adult', 'philosophy', 'biography', 'psychology', 'memoir']
sub_genres = ['alternate-history', 'fairy-tale', 'grimdark', 'epic-fantasy', 'urban-fantasy', 'caper', 'cozy-mystery']
genres = high_genres + sub_genres

for genre in genres:
    path = './data_processing/' + genre + '.pickle'
    books = import_processed_books(path)
    compute_stats(books, genre)