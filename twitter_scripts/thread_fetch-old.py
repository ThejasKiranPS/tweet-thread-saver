import requests
import json
#from twitter_scripts import secrets
#from twitter_scripts import urls
#from twitter_scripts import Write
#from twitter_scripts import fetch_mention
import secrets
import urls
import Write
import fetch_mention

mId='threadsaverbfh'

def auth():
    return secrets.bearer_key


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    # print(response.status_code)
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

    # Write.write(thread_convo, thread_original_tweet,thread_author)

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

    #Write.write_author_only(thread_convo, thread_original_tweet, thread_author)
    #print(f"{thread_original_tweet}\n {thread_convo}")
    return process(thread_convo, thread_original_tweet, thread_author)
    

def process(thread_convo, thread_original_tweet, thread_author):
    userData={}
    conversation_id= thread_original_tweet['data']['id']    
 
    tweet=[]
    tweet.append(thread_original_tweet['data']['text'])
    #print(thread_original_tweet)
    if 'data' in thread_convo.keys():
        thread_convo['data'].reverse()
        #print(thread_convo)
        i=0
        author_id = thread_original_tweet['data']['author_id']

        for t in thread_convo['data']:
            if author_id != t['author_id']:
                break 
            if mId in t['text']:
                break
            tweet.append(t['text'])
    
    userData={
            'thread_author':thread_author['data']['name'],
            'thread_author_username':'@'+thread_author['data']['username'],
            'thread_tweets':tweet,
            'conversation_id': conversation_id,
            }
    # print(userData)
    return userData


def get_threads(twitterUserName):
    ids = fetch_mention.last_mentioned_ids(twitterUserName)
    userData=[]
    for id in ids:
        userData.append(get_thread_author_only(id))
    print(userData)
    return userData
        

#pass twitterUserName in main
def main(twitterUserName):
    data = get_threads(twitterUserName)
    # print(data)
    return data
    #get_thread_author_only(conversation_ids)


def addByUrl(url):
    urlSplit=url.split('status/') 
    return [get_thread_author_only(urlSplit[1])]

if __name__ == "__main__":
    main("thejaskiranps")
