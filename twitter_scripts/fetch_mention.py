import requests
import json

from twitter_scripts import urls
from twitter_scripts import Write
from twitter_scripts import secrets

#import secrets
#import urls
#import Write

def auth():
    return secrets.bearer_key


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

#returns id of tweets from user on which bot was mentioned
def last_mentioned_ids(authorUserName):
    #twitter bot_Username which clients will mention on tweets
    mId='threadsaverbfh'

    #CHANGE NO OF TWEETS TO FETCH HERE
    limit=3

    bearer_token = auth()
    headers = create_headers(bearer_token)

    url = urls.create_author(authorUserName)
    tweets = connect_to_endpoint(url,headers)
    
    conversation_ids=[]
    i=0 
    for tweet in tweets['data']:
        if i>=limit:
            break
        if mId in tweet['text']:
            i+=1
            if tweet['conversation_id'] in conversation_ids:
                continue
            conversation_ids.append(tweet['conversation_id'])
    return conversation_ids
