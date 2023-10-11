
def import_data(filename):
    import pickle

    with open(filename, 'rb') as infile:
        books = pickle.load(infile)

    #books = str(books)
    #print(books)
    return books

def munge_data(books):
    print(books[0])

books = import_data('./data_original/caper.pickle')
munge_data(books)