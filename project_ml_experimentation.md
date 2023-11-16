#### SERX94: Experimentation
#### Book Genre and Subgenre Analysis
#### Dallin Wallace
#### 11/14/2023


## Explainable Records

This will be done on the 'fiction' genre's model 3 (books since 1990).
The model is y = 6.692076773028275e-05x + -0.12814031417098035 
Where x is the publication year and y is the ratio of number of times the book has been shelved in the fiction genre divided by the number of the books has been rated. 

*What the shelved to number of ratings ratio means*
This shelved:num_ratings ratio is a stand-in for genre disctiveness. For specifically, it measures for a particular book and genre how likely that book is be shelved in that genre instead of a different genre. If there was a book that was shelved 50% of the time in romance genre and 50% of the time in the western genre, that book would be less distinct (ie have a lower ratio) in the romance genre than a book that was shelved in romance 90% of the time. It's more complicated than that, as most books aren't shelved in any genre, which leads to VERY small ratios. For readability and comparability, I often multiply the ration by 1000. The highest average ratio for a genre in the entire set is roughly 0.08, which puts the highest distictivness ratio multiplied by 1000 at roughly 100.

The first several books in fiction were all written before 1990, which means they would not be a good pick for this model to predict. The model has a domain of 1990 onwards (for useful information). Some of these books could be put into model 2 for a semi-accurate result, especially since the fiction genre tends to have more older books than most other genres.

I picked the following book titles because they first in the list written after 1990: Harry Potter and the Sorcerer's Stone and The Hunger Games.

### Record 1
**Raw Data:** 
Harry Potter publication date is 1997.
So, the formula is y = 6.692076773028275e-05(1997) + -0.12814031417098035
The result is: 0.005500458986394313
Multiplied by 1000 we get: 5.500458986394313
Looking at the chart of all the average ratios for the fiction genre, the average is roughly 0.005 for fiction, which is exactly where this book lies.


Prediction Explanation:** The fiction genre is very broad, so books shelved in the genre tend to be also shelvable in a popular subgenre, in this case, fantasy. It stands to reason that Harry Potter books get shelved in fantasy often, so it shouldn't be a surprise to find that in the fiction genre, the Harry Potter book has a relatively low disctiveness ratio and around the average for the genre.

### Record 2
**Raw Data:**
The Hunger Games publication date is 2008.
So, the formula is y = 6.692076773028275e-05(2008) + -0.12814031417098035
The result is: 0.0062365874314274095
Multiplied by 1000 we get: 6.2365874314274095
The average for the genre is 0.005 (or 5 if times by 1000)

Prediction Explanation:** The model predict that books have a slightly higher ratio over time. Since 2008 is very recent for the fiction genre, the Hunger Games will have a higher ratio. I think the Hunger Games fits less nicely into a subgenre than Harry Potter, so in the situation, I think it makes sense. Both predictions are close to the average for the genre. 

## Interesting Features
### Feature A
**Feature:** Genre

**Justification:** Genre and Publication Date are the only two factors in determining the model, so they are the two I picked to do expirement with. Each Genre has its own model, so it's actually very easy to see how changing the genre might affect the predicitions.

### Feature B
**Feature:** Publication Date

**Justification:** Genre and Publication Date are the only two factors in determining the model, so they are the two I picked to do expirement with. Publication Date is the input into the genre's model. The goal of using predicition date is to predict what the future of the genre will be like. 

## Experiments 
### Varying A (Genre)
**Prediction Trend Seen:** 
While genres are categorical and thus there isn't any way to increase/decrease "genre", they are still some interesting things to learn from my study of the models across genres. Most genre models are positive, that is increasing in disctiveness. 56 were positive and 26 were negative. In general, the negative models tended to be smaller sub-genres, like cyberpunk or fantasy-romance. Not all sub-genres are negative, though, quite a few (probably about half) are positive. You can see the breakdown in the _overall-summary.txt file in the evaluation folder. You can see a chart of all the coefficients in the __ModelCoefficientComparison.png chart. 

The highest coefficient is from 'cosmere,' which isn't really a genre. It's the name of a fantasy universe from a very popular author. I included as a kind of baseline where a genre is more popular than a single author's universe then it's fairly popular. It makes sense that it is projected to grow in disctiviness, as the author is gaining fans fairly rapidly and his newer books are more popular and interconnected. See the other graph with no cosmere at __ModelCoefficientComparison(No Cosmere).png, als o int the evaluation folder. 

The next highest coefficients are steampunk, pulp, urban-fantasy, middle-grade, travel, and lgbtq. Honestly, I have no idea what these are have in common. They are all fairly small genres. I guess these genres are probably becoming more widely known, thus growing in disctivenss. I guess that makes sense. Maybe we will hear about these genres more and more. 

The lowest coefficients are erotica, cyberpunk, alternate-history, erotic-romance, true-crime, and contemporary-romance. Honestly, I have no idea why these specifically are at the bottom. It find it interesting cyberpunk and steampunk are on complete opposite sides of the spectrum. These genres are getting likely less distinct, meaning they are likely blending with other more popular genres. Like these genres are being overshadowed by another genre. I find this fascinating, though. Many of the genres with the highest ratio are decreasing, which implies that these genres are losing uniquness and blending with other genres, or that maybe these genres are just currently outliers that are correcting back toward a norm. For example, manga, poetry, and parenting are all really high on the average disctiveness ration (see ShelvedRatingsTatioComparison.png in the visuals folder) yet have a decreasing prediction.

### Varying B (Publication Date)
**Prediction Trend Seen:** Varying the date obviously depends on the genre. If we keep the genre 'constant' and vary the date, the predicition will increase and decrease depending of which genre we picked. The one's that are positive are increasing and negative decreasing (see _overall-summary.txt file in the evaluation folder). This one is kind of obvious. For most genres, the ration increases, though for many genres, roughly the same amount (see the visual). It looks a little too flat for a bell curve.

### Varying A and B together
**Prediction Trend Seen:** 
You can't vary genre in a direction like you can publication date. It is impossible to vary them together.

It obvious what's going to happen if you just varied both at the same time. I can see the models. As you vary genre, the output will change randomly, and as you vary publication date, the model will increase of decrease, though often not by a lot. They will not be correlated becuase genre isn't a number and publication date is. I know, unexciting. We already knew the answer. 

### Varying A and B inversely
**Prediction Trend Seen:** It cannot be done since genre is categorically, not a number. You can't go up and down a genre like you can a timeline.

