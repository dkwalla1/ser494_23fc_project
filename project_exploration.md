#### SERX94: Exploratory Data Munging and Visualization
#### The Emergence of Book Subgenres
#### Dallin Wallace
#### 10/16/2023

## Basic Questions
**Dataset Author(s):**
The data set is authored by anonymous readers on the Goodreads website. The readers tag books with certain genres by putting it in a book shelf with the name of the genre. The books are ordered by the0 number of times they have been shelved in that bookshelf, and as I am only scraping some of the book data, the book data I am scraping will come from books which have been likely shelved by multiple people into these shelves.

**Dataset Construction Date:**
The dataset is constructed over time. In essence, the data is constantly changing.

**Dataset Record Count:**
The records depend on the genre. I will by looking at multiple genres, so it depends. For example, fiction has the maximum number of books, 100,000 books, while caper only has 1,139 books.

**Dataset Field Meanings:**
Fields and attributes (which are individual to each book):
 - Image of the book cover
 - Book title
 - Whether the book is in a series OR book type (eg, hardcover, paperback, etc.). It appears that the card only mentions one but not the other. It seems like series has precedence over book type.
 - Book author
 - Whether or not the author is a ‘Goodreads Author’
 - How many times the particular book has been shelved in that particular shelf
 - Average rating of the book
 - Number of ratings of the book
 - Publication date of the book

**Dataset File Hash(es):**
The data was scraped from the Goodreads website with the following patterns of URL: https://www.goodreads.com/shelf/show/{shelf} where {shelf} is the name of the genre shelf being scraped. For example, https://www.goodreads.com/shelf/show/fiction.

I am planning on scraping data for a variety of genres, including: 'fiction', 'non-fiction', 'romance', 'historical', 'fantasy', 'scifi', 'classics', 'mystery', 'thriller', 'young-adult', 'philosophy', 'biography', 'psychology', 'memoir', 'alternate-history', 'fairy-tale', 'grimdark', 'epic-fantasy', 'urban-fantasy', 'caper',  and 'cozy-mystery'. More will likely be added once I analyze the data and figure out what types of genre I want to focus on getting more data for

## Interpretable Records
From the ‘fiction’ shelf:
The records are super easy to understand, so my interpretation isn't very long or complicated

### Record 1
**Raw Data:** See the first book on https://www.goodreads.com/shelf/show/fiction. 

Interpretation:
The first book is 1984 by George Orwell. The average rating is 4.19/5 stars with over 4M ratings. It was published in  1949 and has been shelved as fiction 27,872 times. I think all of these make sense. 1984 is a very popular  fiction book which is why it is the most shelved into a particularly popular shelf. It has been rated millions of times, which makes sense.

### Record 2
**Raw Data:** See the second book on https://www.goodreads.com/shelf/show/fiction. 

**Interpretation:**
The second book is very similar. It is also a classic: To Kill A Mockingbird by Harper Lee. It is also very popular, with over 5M reviews and 27k shelves. The data for a particular book is very intuitive.

## Background Domain Knowledge
While most people understand what a genre of book is, categorizing stories into genres is rather difficult. There are several difficulties with classification of books into a genre. One of which is that genres are very difficult to define. As with many forms of classification there is not a hard border or destinct definition for a particular genre. To one reader, a book might appear to be a mystery. To another, it's a thriller. The most useful genres are both popular and well-known to the public. For example, most people know what the fantasy genre is and common elements fantasy stories have. The fantasy genre is an example of a very useful genre because it communicates what things one can expect from a fantasy story. As an example, a lesser know genre might be a caper, which is 'a subgenre in which the protagonist(s) perpetrate the crime(s). There is usually humor and cleverness involved, along with a sense of adventure' (https://www.servicescape.com/blog/144-genres-and-subgenres-for-fiction-writing). Since a caper is less know, it is less useful to people. In a sense, a genre's usefulness is tied to how commonly it is understood and how popular it is. Thus, over time, we should expect to see the emergence of new genres, as new stories are read and new genres gain wide use. 

This project is seeking to gain insight into the emergence of genres over time, by comparing different points of data about particular genres from the Goodreads website. 

The information gathered from this project can be useful to anyone who wants to categorize or market books. For example, authors can learn about which genres are emerging in popularity that they can write in. Or book publishers can begin using new genre labels for new book releases that provide for specific information to potential consumers. Or libraries can better categorize books for readers looking for something in particular (https://janeyburton.com/why-do-book-categories-book-genres-matter/). Book cover artists also benefit from knowing the book genre, since it's an important part of a book cover to show what style of book it will be (https://www.paperandsage.com/2018/articles/genre-what-is-it-and-why-does-it-matter/).

For more information on the difficulity of classifying genres, see this article: https://journals.ala.org/index.php/lrts/article/view/7455/10285

## Data Transformation

No data transformations were applied. There was one book that didn't have a publication date, but I just gave it 'None' for the date and it was excluded from visualisation. I did not transform it.

### Transformation N
**Description:** TODO

**Soundness Justification:** TODO

(duplicate above as many times as needed; remove this line when done)


## Visualization

### Visual 1: Shelved Comparison

**Analysis:**
This visual compares all the genres together. In particular, it compares the average number of times a book was shelved in a particular genre. This gives an indication of how well-known the genre is, which as discussed in the background knowledge section of this file, is an indication of how useful a genre is. As an example, the first book in the fiction shelf: 1984 by George Orwell was shelved as fiction twenty-seven thousand times. The first book on the caper shelf only was shelved 28 times. This shows that the fiction genre is much more well-known (an thus useful) than the caper genre. 

This chart shows the most well-known genres are as follows: classics, fantasy, fiction, and young-adult. 

What is interesting about this chart is that it differs in one major way from a similar chart: the Genre Strength Comparison chart (see the following section for information on how I calculated Genre Strength). The difference here is that fantasy is much higher in the Shelved Comparison than the Genre Strength Comparison. I intepret this as an indication that the fantasy genre is more well-known than some other genres. This is because the Genre Strength comparison includes the number of reviews as an indication of the number of readers in the genre. So, people who read a fantasy novel are more likely to categorize it as fantasy than people categorizing it as in many other genres. In other words, fantasy has a higher shelved amount to number of ratings ratio. I think this shows that fantasy is very well-known and fantasy stories are easy to identify.

Another interesting point of this chart is that scifi has a very low score. More low than urban-fantasy, which is a very specific genre. I'm not sure if this indicates that scifi is not as popular as fantasy or that it is less well-known as a genre. I suspect the former.

### Visual 2: Genre Strength Comparison

**Analysis:**
This visual compares all the genres together. In particular, it compares the average number of times a book was shelved in a particular genre TIMES the number of ratings in the genre. 

When I first came up with this calculation, I hoped that it would show the 'healthiness' of a genre, by combining the well-know-ness of the genre by comparing the shelved amount and the popularity of the genre by comparing the number of reviews. I fear that this chart actually just accentuates how popular a genre is, since shelved amount and the number of reviews have some of the highest correlation in the correlation matrices. In essence, the shelved amount already has a kind of popularit baked into it, so I was really doing (popularity * well-know-ness) * popularity. I think the chart seems to show this worry I have, as the most popular genres are much higher in comparison to the less popular genres than in the Shelved Comparison. I think the Shelved Comparison might be a better metic of genre 'healthiness.'

This chart shows the most well-known genres are as follows: classics, fiction, fantasy, and young-adult. 

See the Shelved Comparison for more information on differences between this chart and the Shelved Comparison chart.


### Visual 3: Shelved Amount to Publication Date

**Analysis:**
This set of charts seeks to categorize the Shelved Amount to Publication Date. From this we can sense the popularity and well-known-ness of the genre over time. If we see the category increase as time goes on, it provides evidence that the genre is growing and becoming more useful as a category. The opposite is also true— if the category decreases, then it is likely becoming less popular and useful.

Here are some notable charts in this set:

Memoirs seems to be growing or increasing in usefulness. Memoirs published in recent years are being shelved more often an memoirs. I think it makes sense that recent memoirs are more likely to be popular than older ones.

Urban fantasy seems to be decreasing. Maybe urban fantasy is becoming less distinct of a genre?  

The furthest outlier goes to non-fiction with one book in the top 200 from around the year 400.

### Visual 3: Shelved Amount to Number of Reviews

**Analysis:**
Shelved Amount and Number of Reviews are the two attributes which seem to correlate the most. Was can see in several charts a trend more the bottom left to the top right.
 
 One interesting thing I learned from this chart is that there is one book in the cozy-mystery genre that was shelved way fewer times than is normally for the number of ratings. Maybe this book is only borderline 'cozy' and can fit in another genre as well.

### Visual 4: Series

**Analysis:**
There are two types of Series graphs: the histogram graphs and the pie graphs. I find the pie graphs to be easier to understand.

What I found most interesting is that you can see a fairly even split among fiction genres (like fantasy, scifi, etc.) and non-fiction genres (biography, philosophy, etc.). Fiction genres tended to be part of series and non-fiction tended to not be.

Here are the genres which buck this trend:

The fiction genre as a whole is not mostly in series. This is very interesting since most fiction subgenres DID have mostly series. This could be from a couple of things: a) maybe the top fiction books tend to be classics or some other fiction sub-genre which are mostly not in series, b) the sub-genres I pulled from are not a representative of the actual variety of sub-genres and the ones I chose lend themselves to series, c) readers who have a fictional book with no clear sub-genre are more likely to be put it in only the fiction genre AND books with no clear sub-genre are less likely to be in a series (ie this also implies/assumes that readers don't put a book into multiple genres, such as fiction AND grimdark). 

Classics tend to NOT be in series. This implies that series are a more modern format and/or that literary books (which classics tend to be a part of) are more likely to not be in a series. I think that both are likely true. An interesting future visualisation could be series over publication date.

Historical books tend to not be in series, but are fairly evenly split. This make sense as historical books can be either fiction or non-fiction. And historical fiction books are still tied very closely to non-fictional events/times.

Fairy tales are more likely to not be in a series than other fantasy sub-genres. This makes sense to me and might be an indication, like classics, that older books tend to be less likely to be in a series.

Thrillers are mostly not in a series despite being fictional. I'm not sure why this is the case. It may just be a trend in thrillers.

### Visual 4: Shelved Ratings Ratio Comparison

**Analysis:**
This chart was actually made after I started writing this section. As I was analysing the Shelved Comparison and the Genre Strength Comparison, I realize that the popularity of a genre is baked into the shelved amout attribute. This is the reason I said that Genre Strength probably accentuates the difference between popular and less popular genres. 

I made this chart which looked at the ratio between the shelved amount and the number of ratings. The shelved amount is likely a combination of how well-known and distinct a genre is and how popular a genre is. The number of ratings is mostly about how popular a genre is. My dividing the shelved amount by the number of ratings, I am hoping to be able to show the well-know-ness and distinctness of a genre.

The highest genres on this chart are: fantasy, philosophy, classics, urban-fantasy, non-fiction, and cozy-mystery.

I deduced that fantasy must be very well-known/distinct in the analysis of the Shelved Comparison. This graph shows that I am likely right! Fantasy books seem to be shelved more in fantasy than other genres per reviewer. 

I think it makes sense for most of the genres to be here. Fantasy is well-known and easy to apply to a story (eg, does it have magic?). Philosophy is also well-defined and well-known. Classics, urban-fantasy, and non-fiction are also well known and fairly easy to define. I think cozy mystery is the unexepcted result. My thoughts were that the 'coziness' would be hard to define but the data seems to imply this is not the case. 

I find it strange fiction is so low on this graph. My reason for this is that maybe the sub-genres of fiction are more well-known than for non-fiction. People are more likely to shelve a fiction book in a fiction sub-genre that in fiction (and people are unlikely to shelve it in more than one genre). Maybe this is also an indication why the fiction genre is less likely to have series while most fiction sub-genres are likely to have series.








