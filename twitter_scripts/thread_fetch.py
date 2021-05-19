import requests
import json
import secrets
import urls

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

    file= open("./output/convo.txt","w")
    file.write(str(thread_convo))
    file.close()
    file = open("./output/original.txt","w")
    file.write(str(thread_original_tweet))
    file.close()
    file = open("./output/thread.txt","w")
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

def get_thread_author_only(conversation_id):
    bearer_token = auth()
    headers = create_headers(bearer_token)

    url = urls.create_convo(conversation_id)
    thread_convo = connect_to_endpoint(url, headers)

    url = urls.create_id(conversation_id)
    thread_original_tweet = connect_to_endpoint(url, headers)

    author_id = thread_original_tweet['data']['author_id']
    print(author_id)
    url = urls.create_username(author_id)
    thread_author = connect_to_endpoint(url,headers)

    file= open("./output/convo.txt","w")
    file.write(str(thread_convo))
    file.close()
    file = open("./output/original.txt","w")
    file.write(str(thread_original_tweet))
    file.close()
    file = open("./output/thread.txt","w")
    file.write(thread_author['data']['name'])
    file.write('\t')
    file.write('@')
    file.write(thread_author['data']['username'])
    file.write('\n')
    file.write(thread_original_tweet['data']['text'])
    file.write('\n')
    thread_convo['data'].reverse()
    for tweet in thread_convo['data']:
        if tweet['author_id'] == author_id:
            file.write(tweet['text'])
            file.write('\n')
        else:
            break
    
    file.write('\n')
    file.close() 



def main():
    get_thread_author_only('1394668086112833536')

if __name__ == "__main__":
    main()
