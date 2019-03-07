# Sentiment Analysis of Reviews for Yelp Dataset
# Introduction

Given the availability of large volume of online review data, Sentiment Analysis becomes increasingly important.In this project, a sentiment classifier is built which evalutes the polarity of text being either positive or negative or neutral.
Here, we perform sentiment Analysis for reviews of Yelp dataset by proposing a solution using Logistic Regression using Scikit Learn. The preprocessed data is used to find the sentiment of the reviews with the help of a set of positive and negative keywords. 

# Data Preprocessing

The Yelp Dataset is used for this project. Place the "yelp_reviews.csv", "pos_words.txt" and "neg_words.txt" in your working directory to easily import the files into your code. The pre-processing of data includes breaking the sentence into word tokens and removing the stopwords from the tokens.After this, the tokens are compared with set of postive and negative words and scores are assigned. Score '1' for a positive word , '-1' for a negative word and '0' if the word is not present in either of positive or negative words.

Then the mean value of all the words is calculated for all the reviews. The value of mean score helps us to label each review as "Positive", "Negative" or "Neutral"

# Training and Testing of Data

After all the reviews have been identified as positive , negative or neutral, 50000 reviews from the dataset is taken to train and test the model(ratio of 80 and 20).


# Results

From the cross_validation and accuracy scores we can see that our model is able to predict with an accuracy close to 70%.The results on a new data set and the prediction results of our model
