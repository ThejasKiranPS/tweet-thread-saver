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
def create_username(author_id):
    url=f"https://api.twitter.com/2/users/{author_id}"
    return url

def create_author(author):
    query=f"from:{author}"
    tweet_fields = "tweet.fields=text,id,"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    return url

def create_convo(convo_id):
    query =f"conversation_id:{convo_id}"
    tweet_fields = "tweet.fields=author_id,conversation_id,text,id,attachments,in_reply_to_user_id"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    return url

def create_id(id):
    query=f"from:{id}"
    tweet_fields = "tweet.fields=author_id,conversation_id,text,id,created_at,attachments,in_reply_to_user_id"
    
    url = "https://api.twitter.com/2/tweets/{}?tweet.fields=author_id".format(id)
    return url


