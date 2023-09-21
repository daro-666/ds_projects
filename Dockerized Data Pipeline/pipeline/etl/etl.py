import pymongo
from sqlalchemy import create_engine, text
from time import sleep
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sleep(5)

mdb_post_collection = pymongo.MongoClient("reddit_mongodb",port=27017).reddit.datascience
pg_client = create_engine('postgresql://postgres:postgres@reddit_postgresdb:5432/reddit', echo=True).connect()
s = SentimentIntensityAnalyzer()


def init_pg_table():
    """
    creates table in pg db
    """

    create_table = text(
        """
        CREATE TABLE IF NOT EXISTS posts (
        id SERIAL PRIMARY KEY,
        title VARCHAR,
        sentiment NUMERIC
        );
        """
    )
    
    pg_client.execute(create_table)
    pg_client.commit()

def extract_transform_load():
    """
    extracts post titles from mdb and cleans it, calculates composite sentiment score and inserts to pg
    """

    docs = list(mdb_post_collection.find())
    for doc in docs:
    
        title = doc['title'].replace("'", "").replace("&amp;", "and")
        score = s.polarity_scores(title)['compound']
        
        insert = text(f"INSERT INTO posts (title, sentiment) VALUES ('{title}', {score});")
        
        # Execute the query insert
        pg_client.execute(insert)
        pg_client.commit()


init_pg_table()

extract_transform_load()