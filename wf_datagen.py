__author__ = "Dallin Wallace"
__date__ = "10/11/2023"
__assignment = "SER*94: Project"

def web_scrapping(url, classname, outputfile):
    # Import Requests, Beautiful Soup
    import requests
    from bs4 import BeautifulSoup
    import pickle

    attempts = 0
    books = []
    for i in range(4):
        while attempts < 250:
            page_num = f"?page={i+1}"
            r = requests.get(url + page_num)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                books_soup = soup.findAll(class_ = classname)
                for book in books_soup:
                    books.append(book.get_text())
                print(len(books))
            else:
                print("Non 200 status code")
            break
    if (attempts >= 250):    
        print("Could not find loaded comments for this url.")
    with open(outputfile, 'wb') as outfile:
        pickle.dump(books, outfile)

high_genres = ['fiction', 'non-fiction', 'romance', 'historical', 'fantasy', 'scifi', 'classics', 'mystery', 'thriller', 'young-adult', 'philosophy', 'biography', 'psychology', 'memoir']
sub_genres = ['alternate-history', 'fairy-tale', 'grimdark', 'epic-fantasy', 'urban-fantasy', 'caper', 'cozy-mystery']
genres = high_genres + sub_genres

url_t = 'https://www.goodreads.com/shelf/show/'
classname = 'left'
for genre in genres:
    url = url_t + str(genre)
    outfile = "./data_original/" + str(genre) + '.pickle'
    print(genre)
    web_scrapping(url, classname, outfile)