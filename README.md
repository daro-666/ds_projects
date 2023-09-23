## Animated Visualization
In this project I explored the [Gapminder dataset](https://www.gapminder.org/data/) and created an interactive animated plot using [plotly-express](https://plotly.com/python/plotly-express/).

![image](https://github.com/daro-666/ds_projects/assets/128629120/2594ae97-9c26-44f5-8e02-3b6b41112046)

## CV & DeepLearning Classification
Here I used [openCV](https://opencv.org/) to take pictures of objects, trained a CNN using [tensorflow](https://www.tensorflow.org/) to classify said pictures and finally combined the trained model with openCV to make live class predictions on new pictures.

![cv](https://github.com/daro-666/ds_projects/assets/128629120/d1cea0ff-304e-4fd0-92f8-a619a5b8f7e1)

## Classification (Supervised)
Had a go at kaggles famous [Titanic dataset](https://www.kaggle.com/competitions/titanic/overview). Cleaned, selected and engineered relevant features and made survival predictions using several of [scikit-learns](https://scikit-learn.org/) classifiers.

## Dockerized Data Pipeline
Used reddit's api to extract posts from [r/DataScience](https://www.reddit.com/r/datascience/) and saved them in a *postgreSQL* database. Extracted the post titles from the db, ran [sentiment analysis](https://pypi.org/project/vaderSentiment/) on them and uploaded post titles and sentiment scores to a *mongoDB*. Took the contents of the *mongoDB* and wrote a final python script to automate posting the results to a slack channel. Lastly this ETL job was containerized using *docker*.

## Markov Simulation
Created a simulation of customers moving through a fictional supermarket based on markov chain principles through calculating and applying a transition probability matrix. The Supermarket and its customers where implemented as objects.

![image](https://github.com/daro-666/ds_projects/assets/128629120/ea5ec867-92c3-4195-bb99-a77e647a0b36)

## Regression (Supervised)
Taught myself how to handle temporal features using kaggles [bike demand dataset](https://www.kaggle.com/c/bike-sharing-demand). Results had to be evaluated using the RMSLE metric. After trying out several of [scikit-learns](https://scikit-learn.org/) regressors I familiarized myself with [xgboost](https://xgboost.ai/) which yielded in an RMSLE of about 0.46.

## Scraping & NLP
Scraped [lyrics.com](https://www.lyrics.com/) for songtexts of a few artists, cleaned them making heavy use of *regEx* and extracted only contextually meaningful words using one of [spacy's](https://spacy.io/) nlp models. Fitted a naive bayes model to predict artists from songtext snippets an implemented said function in a CLI using *argparse*.  

![image](https://github.com/daro-666/ds_projects/assets/128629120/1b97acd2-7fc4-4d57-9acd-c7a2500f8757)

## Time Series Analysis
Utilized time series analysis methods to make short term predictions on local average temperatures using data from [ecad](https://www.ecad.eu/) which unfortunately containded a lot of intermittent NA's. Compared the results from my from-the-ground-up approach with th results yielded by [statsmodels](https://www.statsmodels.org/) ARIMA model.

![cons_nans](https://github.com/daro-666/ds_projects/assets/128629120/55ec692d-784c-40e1-9ec1-5f9597616956)

## Voice Command CLI
Wrote a python script to ease repeated voice command recordings. Transformed the recordings to the frequency domain within a [tensorflow](https://www.tensorflow.org/) preprocessing pipeline in order to train a NN to classify the voice commands. Created a CLI app to utilize the voice commands to open and close my favorite productivity apps.

[Demo Video](https://drive.google.com/file/d/16pkebYiiXA6RC2bYbBr3PT-4v53DjsMx/view?usp=drive_link)

## WebApp (Unsupervised)
Applied methods of unsupervised learing namely nonlinear-matrix-factorization to build a movie recommender webapp using the streamlit api.

![mr](https://github.com/daro-666/ds_projects/assets/128629120/778dc7af-16d9-482c-8c47-346fceb56fd7)
