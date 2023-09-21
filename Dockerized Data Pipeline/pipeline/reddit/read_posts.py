import requests
import pymongo

from config import tokens


topic = 'datascience'


def get_headers(tokens: dict) -> dict:
    
    """
    creates authentification headers for access via reddit api
    """

    auth = requests.auth.HTTPBasicAuth(tokens['public'], tokens['secret'])
    grant_information = {
                        'grant_type': 'password',
                        'username': tokens['username'],
                        'password': tokens['password']
        }
    headers = {'User-Agent': 'read_posts'}

    at_req = requests.post(
                            'https://www.reddit.com/api/v1/access_token',
                            auth=auth,
                            data=grant_information,
                            headers=headers
        )
    
    if at_req.status_code == 200:

        at = at_req.json()['access_token']

        headers = {**headers, **{'Authorization': f"bearer {at}"}}

        return headers
    
    else:
        print(f"Access token request failed with code: {at_req.status_code}")

        return None
    
def create_mongodb_input(topic: str, headers: dict) -> list:

    """
    downloads reddit posts from r/{topic} and format them for mongodb insertion
    """

    URL = f"https://oauth.reddit.com/r/{topic}/"
    res = requests.get(url=URL, headers=headers)

    if res.status_code == 200:

        res = res.json()
        
        mongo_input = []

        for i, post in enumerate(res['data']['children']):
            title = post['data']['title']
            text = post['data']['selftext']
            mongo_input.append({'_id': i, 'title': title, 'text': text})

        return mongo_input

    else:
        print(f"Data request failed with code: {res.status_code}")
        return None
    
def load_mongodb(mongo_input: list) -> None:

    """
    uploads reddit posts to mongodb
    """

    if type(mongo_input) == list:

        client = pymongo.MongoClient("reddit_mongodb",port=27017)

        collection = client.reddit.datascience

        collection.insert_many(mongo_input)

        print("Insertion successful!")
    else:
        print("Nothing was inserted bc \"mongo_input\" was empty!")


headers = get_headers(tokens)

mongo_input = create_mongodb_input(topic, headers)

load_mongodb(mongo_input)
