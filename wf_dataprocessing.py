import pickle

def import_data(filename):

    with open(filename, 'rb') as infile:
        books = pickle.load(infile)

    #books = str(books)
    #print(books)
    return books

def munge_data(books):
    import re

    p_books = {
        'shelved_avg': -1,
        'shelved_min': -1,
        'shelved_max': -1,

        'rating_avg': -1,
        'rating_min': -1,
        'rating_max': -1,
        
        'pub_date_avg': -1,
        'pub_date_min': -1,
        'pub_date_max': -1,

        'num_ratings_avg': -1,
        'num_ratings_min': -1,
        'num_ratings_max': -1,

        'series_percent': -1,
        'count': 0,
        'books' : {
            #title
            #author
            #rating
            #pub_date
            #shelved
            #series 
        }
    }

    for i, book in enumerate(books):
        #int(re.findall('\d', date)[0])
        rows = book.split('\n')
        title = rows[2]
        series = False
        if '#' in title:
           series = True 
        author = rows[7]
        shelved = re.findall('\d', rows[12])
        shelved = ''.join(map(str, shelved))
        shelved = int(shelved)
        rating = re.findall('\d', rows[16])
        rating = ''.join(map(str, rating))
        rating = rating[:1] + '.' + rating[1:]
        rating = float(rating)
        num_ratings = re.findall('\d', rows[17])
        num_ratings = ''.join(map(str, num_ratings))
        num_ratings = int(num_ratings)
        pub = re.findall('\d', rows[18])
        pub = ''.join(map(str, pub))
        if pub == '':
           pub = None
        else: 
            pub = int(pub)

        p_books['books'][i] = {
            'title': title,
            'author': author,
            'rating': rating,
            'pub_date': pub,
            'shelved': shelved,
            'num_ratings': num_ratings,
            'series': series
        }
        series_num = 0
        if (series):
            series_num = 1
        
        count = p_books['count']
        if count == 0:
            p_books['shelved_avg'] = shelved
            p_books['shelved_min'] = shelved
            p_books['shelved_max'] = shelved

            p_books['rating_avg'] = rating
            p_books['rating_min'] = rating
            p_books['rating_max'] = rating

            p_books['pub_date_avg'] = pub
            p_books['pub_date_min'] = pub
            p_books['pub_date_max'] = pub

            p_books['num_ratings_avg'] = num_ratings
            p_books['num_ratings_min'] = num_ratings
            p_books['num_ratings_max'] = num_ratings

            p_books['series_percent'] = series_num

        p_books['shelved_avg'] = ((p_books['shelved_avg'] * count) + shelved) / (count+1)
        p_books['shelved_min'] = min(p_books['shelved_min'], shelved)
        p_books['shelved_max'] = max(p_books['shelved_max'], shelved)

        p_books['rating_avg'] = ((p_books['rating_avg'] * count) + rating) / (count+1)
        p_books['rating_min'] = min(p_books['rating_min'], rating)
        p_books['rating_max'] = max(p_books['rating_max'], rating)

        if pub != None:
            p_books['pub_date_avg'] = ((p_books['pub_date_avg'] * count) + pub) / (count+1)
            p_books['pub_date_min'] = min(p_books['pub_date_min'], pub)
            p_books['pub_date_max'] = max(p_books['pub_date_max'], pub)

        p_books['num_ratings_avg'] = ((p_books['num_ratings_avg'] * count) + num_ratings) / (count+1)
        p_books['num_ratings_min'] = min(p_books['num_ratings_min'], num_ratings)
        p_books['num_ratings_max'] = max(p_books['num_ratings_max'], num_ratings)

        p_books['series_perent'] = ((p_books['series_percent'] * count) + series_num) / (count+1)

        p_books['count'] += 1

        print(title, author, shelved, rating, pub, num_ratings, series)
        print(p_books['shelved_avg'], p_books['rating_avg'], p_books['pub_date_avg'], p_books['num_ratings_avg'], p_books['series_percent'])

    return p_books
        # for i, row in enumerate(rows):
        #      print(str(i) + ' ' + rows[i])

high_genres = ['fiction', 'non-fiction', 'romance', 'historical', 'fantasy', 'scifi', 'classics', 'mystery', 'thriller', 'young-adult', 'philosophy', 'biography', 'psychology', 'memoir']
sub_genres = ['alternate-history', 'fairy-tale', 'grimdark', 'epic-fantasy', 'urban-fantasy', 'caper', 'cozy-mystery']
genres = high_genres + sub_genres

for genre in genres:
    path = './data_original/' + genre + '.pickle'
    books = import_data(path)
    p_books = munge_data(books)
    path = './data_processing/' + genre + '.pickle'
    with open(path, 'wb') as outfile:
        pickle.dump(p_books, outfile)