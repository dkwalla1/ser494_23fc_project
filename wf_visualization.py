import pickle

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
    print(books['series_percent'])
    for book in books['books']:
        max_rating = -1
        min_rating = 6
        # print(books['books'][book]['rating'])
        # #max_rating = max(max_rating, book['rating'])
        # #min_rating = min(min_rating, book['rating'])
        # print(genre)
        # print(max_rating)
        # print(min_rating)
        #print(book['avg_rating'])


high_genres = ['fiction', 'non-fiction', 'romance', 'historical', 'fantasy', 'scifi', 'classics', 'mystery', 'thriller', 'young-adult', 'philosophy', 'biography', 'psychology', 'memoir']
sub_genres = ['alternate-history', 'fairy-tale', 'grimdark', 'epic-fantasy', 'urban-fantasy', 'caper', 'cozy-mystery']
genres = high_genres + sub_genres

for genre in genres:
    path = './data_processing/' + genre + '.pickle'
    books = import_processed_books(path)
    compute_stats(books, genre)