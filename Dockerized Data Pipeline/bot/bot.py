from sqlalchemy import create_engine, text
from time import sleep
from decimal import Decimal
import requests

from config import hookurl


sleep(10)

pg_client = create_engine('postgresql://postgres:postgres@reddit_postgresdb:5432/reddit', echo=True).connect()


def bot_post():

    """
    queries pg for all posts, selects first one not pinned, posts to slack
    """

    myquery = text(
        """
        SELECT title, sentiment FROM posts; 
        """    
    )

    q_res = pg_client.execute(myquery).fetchall()

    #print(q_res)

    ans_f_davidbot = f"Post Title: {q_res[1][0]} | Sentiment: {q_res[1][1]}"

    print(ans_f_davidbot)

    #data = {'text': ans_f_davidbot}

    #requests.post(url = hookurl, json = data)


bot_post()


