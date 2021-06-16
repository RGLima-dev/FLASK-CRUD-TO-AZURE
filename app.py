from src.server.instance import *
from src.Controller.CRUD import *

server = Server()

#WHEN U UP SOMETHING IN AZURE, REMOVE THE .RUN -> AZURE WILL RUN IT FOR YOU
#I JUST LET THIS APP.RUN TO YOU TEST BEFORE DEPLOY IN AZURE
app.run()
