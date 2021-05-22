mId='@amalpaultech'
def write_author_only(thread_convo, thread_original_tweet, thread_author):
    file= open("./output/convo.txt","w")
    file.write(str(thread_convo))
    file.close()
    
    file = open("./output/original.txt","w")
    file.write(str(thread_original_tweet))
    file.close()
    author_id = thread_original_tweet['data']['author_id']
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
            if mId in tweet['text']:
                continue
            file.write(tweet['text'])
            file.write('\n')
        else:
            break
    
    file.write('\n')
    file.close()

def write(thread_convo, thread_original_tweet, thread_author):
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

#useless wrong function below (dont delete)
def get(thread_convo, thread_original_tweet, thread_author):
    userData=[]

    for i in range(3):
        userData[i]={
                'thread_author':thread_author['data']['name'],
                'thread_tweets':thread_tweets,
                'conversation_id': conversation_id,
                }


    file.write('\n')
    file.close()

