# views.py
from django.shortcuts import render, redirect
from pymongo import MongoClient

# Connect to the MongoDB database
cluster = MongoClient(
    'mongodb+srv://ibinabobliss:barawot90@cluster0.xnbkjyg.mongodb.net/?retryWrites=true&w=majority')
db = cluster['chats']
collection = db['chats']


def welcomescreen(request):
    return render(request, 'welcome.html')


def HomePage(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']

        # Check if the room exists in MongoDB
        if db.rooms.find_one({'room_name': room}):
            return redirect("room", room_name=room, username=username)
        else:
            # If the room doesn't exist, create it in MongoDB
            db.rooms.insert_one({'room_name': room})
            return redirect("room", room_name=room, username=username)

    return render(request, 'index.html')


def message_room(request, room_name, username):
    # Get the room ObjectId from MongoDB
    room = db.rooms.find_one({'room_name': room_name})

    if request.method == 'POST':
        message = request.POST['message']

        # Insert the message into the MongoDB messages collection
        db.messages.insert_one(
            {'room_id': room['_id'], 'sender': username, 'message': message})

    # Get all messages for the room from MongoDB
    messages = list(db.messages.find({'room_id': room['_id']}))

    context = {
        "messages": messages,
        "user": username
    }
    return render(request, 'message.html', context)
