import os
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
    NUM_PAGES_TO_READ = 16 #<-- the number of pages with 50 books read (Ex: 4, means 200 books are read from that shelf) (Except for dystopian for some reason only has 49 books to a page 🤷‍♂️)
    for i in range(NUM_PAGES_TO_READ): 
        while attempts < 250:
            page_num = f"?page={i+1}"
            r = requests.get(url + page_num)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                books_soup = soup.findAll(class_ = classname)
                for book in books_soup:
                    books.append(book.get_text())
                print(len(books), '/', NUM_PAGES_TO_READ*50)
            else:
                print("Non 200 status code")
            break
    if (attempts >= 250):    
        print("Could not find loaded comments for this url.")
    with open(outputfile, 'wb') as outfile:
        pickle.dump(books, outfile)

def generate_data(genres):
    url_t = 'https://www.goodreads.com/shelf/show/'
    classname = 'left'
    for genre in genres:
        url = url_t + str(genre)
        outfile = '.'  + os.sep + 'data_original'  + os.sep + str(genre) + '.pickle'
        print(genre)
        web_scrapping(url, classname, outfile)


genres = []

with open('genres.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    if line[0] == '#' or line[0] == '\n':
        continue
    genres.append(line.replace('\n', ''))

generate_data(genres)