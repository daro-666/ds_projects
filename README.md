## Animated Visualization
In this project I explored the [Gapminder dataset](https://www.gapminder.org/data/) and created an interactive animated plot using [plotly-express](https://plotly.com/python/plotly-express/).

![gm](https://github.com/daro-666/ds_projects/assets/128629120/263036e2-54b0-4f66-b758-ba172a386474)

## CV & DeepLearning Classification
Here I used [openCV](https://opencv.org/) to take pictures of objects, trained a CNN using [tensorflow](https://www.tensorflow.org/) to classify said pictures and finally combined the trained model with openCV to make live class predictions on new pictures.

![cv](https://github.com/daro-666/ds_projects/assets/128629120/b36a44d2-a385-4960-8777-3b3f843e9888)

## Classification (Supervised)
Had a go at kaggles famous [Titanic dataset](https://www.kaggle.com/competitions/titanic/overview). Cleaned, selected and engineered relevant features and made survival predictions using several of [scikit-learns](https://scikit-learn.org/) classifiers.

## Dockerized Data Pipeline
Used reddit's api to extract posts from [r/DataScience](https://www.reddit.com/r/datascience/) and saved them in a *postgreSQL* database. Extracted the post titles from the db, ran [sentiment analysis](https://pypi.org/project/vaderSentiment/) on them and uploaded post titles and sentiment scores to a *mongoDB*. Took the contents of the *mongoDB* and wrote a final python script to automate posting the results to a slack channel. Lastly this ETL job was containerized using *docker*.

## Markov Simulation
Created a simulation of customers moving through a fictional supermarket based on markov chain principles through calculating and applying a transition probability matrix. The Supermarket and its customers where implemented as objects.

![customers](https://github.com/daro-666/ds_projects/assets/128629120/db133724-0ad2-4d48-98f0-1c1e4388e74f)

## Regression (Supervised)
Taught myself how to handle temporal features using kaggles [bike demand dataset](https://www.kaggle.com/c/bike-sharing-demand). Results had to be evaluated using the RMSLE metric. After trying out several of [scikit-learns](https://scikit-learn.org/) regressors I familiarized myself with [xgboost](https://xgboost.ai/) which yielded in an RMSLE of about 0.46.

## Scraping & NLP
Scraped [lyrics.com](https://www.lyrics.com/) for songtexts of a few artists, cleaned them making heavy use of *regEx* and extracted only contextually meaningful words using one of [spacy's](https://spacy.io/) nlp models. Fitted a naive bayes model to predict artists from songtext snippets an implemented said function in a CLI using *argparse*.  

![Screenshot from 2023-09-23 13-53-41](https://github.com/daro-666/ds_projects/assets/128629120/50750766-e342-4696-b527-8aea77790494)

## Time Series Analysis
Utilized time series analysis methods to make short term predictions on local average temperatures using data from [ecad](https://www.ecad.eu/) which unfortunately containded a lot of intermittent NA's. Compared the results from my from-the-ground-up approach with the results yielded by [statsmodels](https://www.statsmodels.org/) ARIMA model.

![cons_nans](https://github.com/daro-666/ds_projects/assets/128629120/90775c15-258a-40c9-ad53-e0f035131ed2)

## Voice Command CLI
Wrote a python script to ease repeated voice command recordings. Transformed the recordings to the frequency domain within a [tensorflow](https://www.tensorflow.org/) preprocessing pipeline in order to train a NN to classify the voice commands. Created a CLI app to utilize the voice commands to open and close my favorite productivity apps.

[Demo Video](https://drive.google.com/file/d/16pkebYiiXA6RC2bYbBr3PT-4v53DjsMx/view?usp=drive_link)

## WebApp (Unsupervised)
Applied methods of unsupervised learing namely non-negative-matrix-factorization to build a movie recommender webapp using the streamlit api. Movie data was taken from the [movielens dataset](https://grouplens.org/datasets/movielens/latest/)

![mr](https://github.com/daro-666/ds_projects/assets/128629120/4af5046b-5059-4aea-9173-f0d8d68eba3b)
