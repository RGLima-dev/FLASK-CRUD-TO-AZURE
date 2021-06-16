from os import name
from re import S
from flask import Response,request
import json
from src.server.instance import Server

db = Server.db
app = Server.app

class Usuario(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))

    #Transform In Json
    def toJson(self):
        return {"id": self.id, "name": self.nome, "email:": self.email}


def generateStatus(status, content, message=False):
    body = {}
    body["content"] = content

    if(message):
        body["message"] = message

    return Response(json.dumps(body), status= status, mimetype="application/json")


#INDEX
@app.route("/", methods=["GET"])
def index():
    return 'GET ALL -> Use /users/  ** GET BY ID -> /users/id    ** POST -> /users/    ** PUT -> /users/id **   DELETE -> /users/id'


#GET
@app.route("/users/", methods=["GET"])
def get_all():
    users_class = Usuario.query.all()
    users_json = [user.toJson()for user in users_class]
    return generateStatus(200,users_json, "")

# GETBYID
@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = Usuario.query.filter_by(id=id).first()
    user_json = user.toJson()
    
    return generateStatus(200,user_json,"ok")

#POST
@app.route("/users", methods=["POST"])
def create_user():
    body = request.get_json(force=True)

    try:
        user = Usuario(nome=body["nome"], email=body["email"])
        Server.db.session.add(user)
        Server.db.session.commit()
        return generateStatus(201,user.toJson(), "User created")

    except Exception as e:
        print(e)
        return generateStatus(400,{}, "Failed to Create a new user")

#PUT
@app.route("/users/<id>", methods=["PUT"])
def Put_user(id):
    user = Usuario.query.filter_by(id=id).first()
    body=request.get_json(force=True)
    try:
        if('nome' in body):
            user.nome = body["nome"]
        if('email' in body):
            user.email = body["email"]

        Server.db.session.add(user)
        Server.db.session.commit()
        return generateStatus(200,user.toJson(), "User Updated with Sucess")

    except Exception as e:
        print(e)
        return generateStatus(400,{}, "Failed to update a new user")

#DELETE
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    user = Usuario.query.filter_by(id=id).first()

    try:
        Server.db.session.delete(user)
        Server.db.session.commit()
        return generateStatus(200,user.toJson(), "User Deleted with Sucess")

    except Exception as e:
        print(e)
        return generateStatus(400,{}, "Failed to Delete a new user")