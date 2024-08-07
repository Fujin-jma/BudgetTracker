'''

This section is for the configurations of the app


'''

'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)  #To prevent that error he was talking about between servers
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projdatabase.db" 
#specifying the location of the local sequalite database in our machine
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
#to inform that we don't want to track any modifications in our database


db = SQLAlchemy(app) #makes an instance of the database above (from SQLALchemy)

'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()   #makes an instance of the database above (from SQLALchemy)

def createapp():
    app = Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projdatabase.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    return app


