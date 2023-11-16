import pymongo
from pymongo import mongo_client

cluster = mongo_client("mongodb+srv://ibinabobliss:<password>@cluster0.xnbkjyg.mongodb.net/?retryWrites=true&w=majority")
db = cluster("room")
collection =db("room")



collection.insert_one({})

from pymongo import MongoClient
from django.shortcuts import render, redirect
from .models import Room, Message

# MongoDB connection
client = MongoClient(host='your_mongodb_host', port=your_mongodb_port, username='your_mongodb_username', password='your_mongodb_password')
db = client['your_mongodb_database']

# ...

def HomePage(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']

        # Use pymongo to check if the room exists
        if db['Room'].find_one({'room_name': room}):
            return redirect("room", room_name=room, username=username)
        else:
            # Create the room using pymongo
            db['Room'].insert_one({'room_name': room})
            return redirect("room", room_name=room, username=username)

    return render(request, 'index.html')

# ...

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ibinabobliss:<password>@cluster0.xnbkjyg.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)