import numpy as np
import pandas as pd
from joblib import load
from fuzzywuzzy import process, fuzz
import logging



logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s')



movies  = pd.read_csv("../data/movies.csv", index_col=0)
movies.drop(columns='genres', inplace=True)

ratings = pd.read_csv("../data/ratings.csv", index_col=0)
ratings.drop(columns='timestamp', inplace=True)

model = load("../models/nmf_model")



def id_to_title(id:int)-> str:
    return movies.loc[id][0]


def title_to_id(title:str) -> int:
    return movies.index[movies['title'] == title][0]


def ratings_to_R(ratings:pd.DataFrame, min_ratings=20) -> pd.DataFrame:
    '''converts ratings DataFrame into right format for NMF
    '''
    ratwide = ratings.pivot(columns='movieId', values='rating')
    ratwide_filtered = ratwide.dropna(axis=1, thresh=min_ratings)
    R = ratwide_filtered.fillna(ratwide_filtered.mean())

    return R


def movies_filter(R:pd.DataFrame) -> pd.DataFrame:
    '''creates a new filtered movies reference dataframe based on filtering applied for R-matrix creation
    '''
    return movies.loc[ratings_to_R(ratings).columns]


def search_for_mov(movie:str) -> pd.DataFrame:
    '''search for movie titles in the filtered movielist 
    '''
    return movies_filter(ratings_to_R(ratings))[movies_filter(ratings_to_R(ratings))['title'].str.contains(movie)]


def convert_user(user:dict) -> dict:
    '''converts movie titles to ids in a user ratings dict
    '''
    conv_user = {}
    items = user.items()

    for item in items:
        conv_user.update({title_to_id(item[0]): item[1]})
    
    return conv_user


def user_dicttoDF(user:dict) -> pd.DataFrame:
    '''creates a dataframe from a userdict that matches the feature dimension of
       the ratings dataframe
    '''
    user = convert_user(user)

    movieIds = list(ratings_to_R(ratings).columns)
    empty_list = [np.nan]*len(movieIds)
    ratings_dict = dict(zip(movieIds, empty_list))

    for movie, rating in user.items():
        ratings_dict[movie] = rating

    user_df = pd.DataFrame(list(ratings_dict.values()), index=movieIds)
    user_df.columns = ['rating']

    return user_df


def fill_user_df(user_df:pd.DataFrame, value=0.0):
    '''fills NaN's in user df with specified value
    '''
    user_df_filled = user_df.fillna(value)
    user_df_filled = user_df_filled.T

    return user_df_filled


def get_recs(user_df_filled:pd.DataFrame) -> pd.DataFrame:
    '''create the dataframe with predicted ratings for recommendation
    '''
    user_P = model.transform(user_df_filled)
    Q = model.components_
    preds = np.dot(user_P,Q)
    recs = pd.DataFrame(preds, columns=user_df_filled.columns)

    return recs


def format_recs(user_df:pd.DataFrame, recs:pd.DataFrame) -> pd.DataFrame:
    '''filters out movies the user has already rated and formats the output dataframe ready for display
    '''
    # mask creation
    not_rated_mask = np.isnan(user_df.T.values[0])
    not_rated = recs.columns[not_rated_mask]
    # apply mask to recommendations
    items_to_recommend = recs[not_rated].T
    # naming, sorting, formatting
    items_to_recommend.columns = ['predicted_rating']
    items_to_recommend_sorted = items_to_recommend.sort_values(by='predicted_rating', ascending=False)
    items_to_recommend_sorted['predicted_rating'] = items_to_recommend_sorted['predicted_rating'].map(lambda x: round(x,2))
    items_to_recommend_sorted.reset_index(names='movie_title', inplace=True)
    items_to_recommend_sorted['movie_title'] = items_to_recommend_sorted['movie_title'].map(lambda x: id_to_title(x))
    items_to_recommend_sorted.index = items_to_recommend_sorted.index + 1

    return items_to_recommend_sorted


def nmf_predict(user:dict, n_recs=10, fillNanValue=0.0) -> pd.DataFrame:
    '''successive use of functions to make recommendation. see used functions descriptions for details
    '''
    
    user_processed = user_process(user)
    user_df = user_dicttoDF(user_processed)
    user_df_filled = fill_user_df(user_df, fillNanValue)
    recs = get_recs(user_df_filled)
    output = format_recs(user_df, recs)

    return output.loc[:n_recs]


def user_process(user:dict) -> dict:
    '''uses fuzzywuzzy to pick best matching movie title from user input
    '''
    user_processed = {}
    
    for movie, rating in user.items():
        best_match, score = process.extractOne(movie, list(movies_filter(ratings_to_R(ratings))['title'].values), scorer=fuzz.token_set_ratio)
        user_processed[best_match] = float(rating)
        
        if score < 70:
            logging.warning(f'Not sure I found the right movie title for: "{movie}"')

    return user_processed