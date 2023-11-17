#this is our configuration folder to configure flask to our app location & variables needed to run Flask 


from datetime import timedelta
import os #operating system
from dotenv import load_dotenv #allows us to load environment variables to do certain things with our app

#establish our base dirctory so whenever we use "." to reference any loction in our app it knows we are referening
#rangers_shop folder
basedir = os.path.abspath(os.path.dirname(__file__)) #this is establishing our base directory or our root folder


#need to establish where our environment variables are coming from(this file will be hidden from github)
load_dotenv(os.path.join(basedir, '.env')) #this is just pointing us to the direction of our environment variables (located in .env file)



#create our Config class
class Config():
    """
    Create Config class which will setup our configuration other create config variables.
    Using environment variables where avaible other create config variables.
    """

    #regular configuration for Flask App
    FLASK_APP = os.environ.get('FLASK_APP') #looking for the key of Flask_APP in our .env file 
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")

    #configuration if you are connecting a database
    SECRET_KEY = os.environ.get('SECRET_KEY') or "Literally whatever you want as long as its a string. Cool Beans"  "Nana nana boo boo, you'll never guess this" 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #we dont want a message every single time our database is changed
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)

