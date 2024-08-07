'''

We want a CRUD: Create, read, update, delete


'''

#uses flask to do requests and jsonify stuff
from flask import request, jsonify

#implements stuff from other python files
from config import createapp, db
from models import Contact

app = createapp()

@app.route("/contacts", methods=["GET"]) #decorater, specifies the route and valid methods
def get_contacts():
    contacts = Contact.query.all() #gets all of different contacts
    json_contacts = list(map(lambda x: x.to_json(), contacts)) 
    #lambda is to write a function in one line
    #map returns a new map object so we do list
    return jsonify({"contacts": json_contacts})

#post method

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    
    if not first_name or not last_name or not email:
        return(
            jsonify({"message": "Include all first name, last name and email."}), 400,
        )



if __name__ == "__main__":

    #creates the database
    with app.app_context():
        db.create_all()
    app.run(debug=True) #runs flask