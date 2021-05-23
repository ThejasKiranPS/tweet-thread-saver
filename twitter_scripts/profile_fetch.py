import tweepy
import secrets

# Authenticate to Twitter
auth = tweepy.OAuthHandler(secrets.api_key, secrets.api_secret_key)
auth.set_access_token(secrets.access_token, secrets.access_token_secret)

# Create API object 
api = tweepy.API(auth)

def check_authentication():
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")


def get_profile_url(screenname):
    user = api.get_user(screenname)
    image_url = user.profile_image_url_https.replace("_normal", "")
    print(image_url)
    return image_url


if __name__ == "__main__":
    get_profile_url("amalpaultech")