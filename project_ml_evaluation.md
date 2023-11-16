#### SERX94: Machine Learning Evaluation
#### Book Genre and Subgenre Analysis
#### Dallin Wallace
#### 11/14/2023

The model is linear regression, by the way.

## Evaluation Metrics
### Metric 1
**Name:** MSE (Mean Squared Error)

**Choice Justification:** This is the average squared distance each point is from the line created by the linear regression model. I chose this because it helps show how well modelled the data is. If we have a low MSE, it means that the model fits to the data well. If we have a high MSE, it shows that the model does not fil the data well. MSE has an effect where points further from the model increase the MSE more. 

Interpretation:** Well, I have a collection of models because each genre needs its own model and there a whole bunch of genres. For each model, the lower the MSE, the better. In comparison with MAE, a high MSE but lower MAE means that there are points which are more distant (a higher variance). 

### Metric 2
**Name:** MAE (Mean Absoulte Error)

**Choice Justification:** This is the average of the absolute difference between the data points and the model predicitions. MAE is the average distance a predicition will be from the actual value. I chose this because it is more understandable than MSE and gives a different interpretation of error. MSE can help show the amount of outliers, while MAE can act like an average distance from the model predicition.

Interpretation:** Well, I have a collection of models because each genre needs its own model and there a whole bunch of genres. For each model, the lower the MAE, the better. The MAE will be the average distance a predicition will be from the actual value. If the MSE if way bigger than the MAE, that shows that there are outliers.

## Alternative Models
### Alternative 1: All
**Construction:** This model is trained on all the book data for that genre. As a reminder, the book data is currently the most rated books in that genre. Currently I have the number of books to scrape to be 800 but that might change. So, this model is trained on the data across all 800.

**Evaluation:** For many of the genres, there are only a couple books that aren't included in the other genres. As such, this model is mostly the same as the other models. In cases where it is not the same, it is ignoring books from the past. This model MIGHT perform better for books in the far past, though there are so few of them, that the model will likely be incorrect. The books in the far past in the data are "classics," which will not be representative of the actual spread of data in the past. 

The MSE and MAE are predictably very similar across all models. I think this model's MSE and MAE tend to be ever so slightly worse since the far past books probably tend to be outliers. I think in general this model is actually the least helpful of the three since the past data in Goodreads is so biased.

## Alternative Models
### Alternative 2: Books later than 1940
**Construction:** The model is trained on all the books that were published after 1940, to reduce the influence of outliers.

**Evaluation:** I think this model is helpful because it takes into account all semi-recent books. I think it is ultimaetly less helpful than model 3 because, even though these genres have several books from 1940-1990 I think it's still not as common as it needs to be to show model future trends. This model is obviously helpful if you want to make a predicition in the 1970s-1990s.

The MSE and MAE are predictably very similar across all models.


## Alternative Models
### Alternative 3: Books later than 1990
**Construction:** This model is trained on all books that were published after 1990, in order to focus on the more recent books, which Goodreads tends toward. 

**Evaluation:** I think this model is most helpful for predicting future trends because it takes into account the section of data which is most unbiased in Goodreads and is more focused on the recent trends. This is obviously noy helpful for analysing trends before 1990.

The MSE and MAE are predictably very similar across all models.


## Visualization
There are currently no visuals, though they would be fascinating if I had more time.

## Best Model

**Model:** Model 3 (unless you specifically want to predict for times in roughly the 1970s-1990s, which might not have that good of predictions anyway)