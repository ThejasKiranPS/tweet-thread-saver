import requests
import json
from twitter_scripts import secrets
from twitter_scripts import urls
from twitter_scripts import Write
from twitter_scripts import fetch_mention

def auth():
    return secrets.bearer_key


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def get_thread(conversation_id):
    bearer_token = auth()
    headers = create_headers(bearer_token)

    url = urls.create_convo(conversation_id)
    thread_convo = connect_to_endpoint(url, headers)

    url = urls.create_id(conversation_id)
    thread_original_tweet = connect_to_endpoint(url, headers)

    author_id = thread_original_tweet['data']['author_id']
    # print(auth)
    url = urls.create_username(author_id)
    thread_author = connect_to_endpoint(url,headers)

    Write.write(thread_convo, thread_original_tweet,thread_author)

def get_thread_author_only(conversation_id):
    bearer_token = auth()
    headers = create_headers(bearer_token)

    url = urls.create_convo(conversation_id)
    thread_convo = connect_to_endpoint(url, headers)

    url = urls.create_id(conversation_id)
    thread_original_tweet = connect_to_endpoint(url, headers)

    author_id = thread_original_tweet['data']['author_id']
    #print(author_id)
    url = urls.create_username(author_id)
    thread_author = connect_to_endpoint(url,headers)

    # Write.write_author_only(thread_convo, thread_original_tweet, thread_author)
    print(f"{thread_original_tweet['text']}\n {thread_convo}")


#pass twitterUserName in main
def main(twitterUserName= 'thejaskiranps'):
    conversation_id = fetch_mention.last_mentioned_id(twitterUserName)
    get_thread_author_only(conversation_id)

if __name__ == "__main__":
    main()
