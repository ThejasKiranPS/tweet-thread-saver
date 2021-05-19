import requests
import json
import secrets
import urls
import Write

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
    print(author_id)
    url = urls.create_username(author_id)
    thread_author = connect_to_endpoint(url,headers)

    Write.write_author_only(thread_convo, thread_original_tweet, thread_author)



def main():
    get_thread_author_only('1394668086112833536')

if __name__ == "__main__":
    main()
