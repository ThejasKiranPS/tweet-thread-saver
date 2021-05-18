import requests
import json
import secrets

def auth():
    return secrets.bearer_key

def create_url():
    query ="from:thejaskiranps"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=author_id,conversation_id,text,id,created_at,attachments,in_reply_to_user_id"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    return url
def create_url_username(author_id):
    url=f"https://api.twitter.com/2/users/{author_id}"
    return url

def create_url_author(author):
    query=f"from:{author}"
    tweet_fields = "tweet.fields=text,id,"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    return url

def create_url_convo(convo_id):
    query =f"conversation_id:{convo_id}"
    tweet_fields = "tweet.fields=author_id,conversation_id,text,id,attachments,in_reply_to_user_id"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    return url

def create_url_id(id):
    query=f"from:{id}"
    tweet_fields = "tweet.fields=author_id,conversation_id,text,id,created_at,attachments,in_reply_to_user_id"
    
    url = "https://api.twitter.com/2/tweets/{}?tweet.fields=author_id".format(id)
    return url


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

    url = create_url_convo(conversation_id)
    thread_convo = connect_to_endpoint(url, headers)

    url = create_url_id(conversation_id)
    thread_original_tweet = connect_to_endpoint(url, headers)

    author_id = thread_original_tweet['data']['author_id']
    print(auth)
    url = create_url_username(author_id)
    thread_author = connect_to_endpoint(url,headers)
    
    file= open("convo.txt","w")
    file.write(str(thread_convo))
    file.close()
    file = open("original.txt","w")
    file.write(str(thread_original_tweet))
    file.close()
    file = open("thread.txt","w")
    file.write(thread_author['data']['name'])
    file.write('\t')
    file.write('@')
    file.write(thread_author['data']['username'])
    file.write('\n')
    file.write(thread_original_tweet['data']['text'])
    file.write('\n')
    thread_convo['data'].reverse()
    for tweet in thread_convo['data']:
        file.write(tweet['text'])
        file.write('\n')
    
    file.write('\n')
    file.close() 


def main():
    get_thread('1394668086112833536')

if __name__ == "__main__":
    main()