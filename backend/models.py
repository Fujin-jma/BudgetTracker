'''

This section is for the database. To know which fields we need, 
how to add them, delete them, manipulate them.


'''

'''
from config import db

class Contact(db.Model):   #going to import from db.Model
    id = db.Column(db.Integer, primary_key=True)  
    #specifies type of integer and classifies it as a primary key

    #has properties, the integers are max characters
    first_name = db.Column(db.String(80, unique=False, nullable=False)) 
    last_name = db.Column(db.String(80, unique=False, nullable=False))
    email = db.Column(db.String(200, unique=True, nullable=False))

    #needs to pass it as json to api
    def to_json(self):
        return{
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }
 

'''

from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #specifies type of integer and classifies it as a primary key
    
    #has properties, the integers are max characters
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)

    #needs to pass it as json to api
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }
