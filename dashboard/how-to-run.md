# tweet-thread-saver

### How to run tweet-thread-saver django site on your local machine

Make sure you have python3 installed on you computer if you don't know run the command below to check python version

```bash
python3 --version
```

If you have anything below 3.5 install python3 latest version by running commands below

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt updates
sudo apt install python3.9
python3.9 --version
```

Now you should see something like Python 3.9 when you run the first command to check python version

Now we will have to use a virtual environment to install all the dependencies without effecting other packages in you system

These command will now create new virtual environment in your current folder and activate them

```bash
sudo apt install python3-venv
python3 -m venv tweetthreadsaver-env
source tweetthreadsaver-env/bin/activate

```

Once you have activated your virtual environment clone the respository

```bash
git clone https://github.com/ThejasKiranPS/tweet-thread-saver.git
cd tweet-thread-saver
git checkout deploy
```

Once you are in the tweet-thread-saver folder you will need to install all the required dependencies

to do that run the commands below

```bash
pip install -r requirements.txt
```

You will need a twitter developers account to use the twitter API used in this project the [secrets.py](http://secrets.py) should be included in the twitter_scripts folder 

```python
api_key = 'api_key' 
api_secret_key = 'api_secret_key'
bearer_key = 'bearer_key'
access_token = 'access_token'
access_token_secret = 'access_token_secret'
```

Once you have installed all the dependencies for the project and saved  the [secrets.py](http://secrets.py) file with your credentials you will need to create a database for the project by running

```bash
python manage.py makemigrations
python manage.py migrate
```

Once you have migrated the database you can start the development server just by running

```bash
python manage.py runserver
```

Now you will see a url in your terminal you can open the link just by clicking the link it will take you the homepage of the website
