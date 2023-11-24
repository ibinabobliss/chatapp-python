# decorators.py

from django.shortcuts import render, redirect
from pymongo import MongoClient
from django.http import HttpResponseServerError


def welcomescreen(request):
    return render(request, 'welcome.html')


def connect_to_mongodb():
    cluster = MongoClient(
        'mongodb+srv://ibinabobliss:barawot90@cluster0.xnbkjyg.mongodb.net/?retryWrites=true&w=majority')
    db = cluster['chats']
    return db['chats']


db = connect_to_mongodb()


def HomePage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        room = request.POST.get('room')

        try:
            # Check if the room exists in MongoDB
            existing_room = db.rooms.find_one({'room_name': room})

            if existing_room:
                return redirect("room", room_name=room, username=username)
            else:
                # If the room doesn't exist, create it in MongoDB
                new_room = db.rooms.insert_one({'room_name': room})
                if not new_room.inserted_id:
                    raise ValueError("Failed to create room in the database")

                return redirect("room", room_name=room, username=username)

        except Exception as e:
            return HttpResponseServerError(f"Error: {str(e)}")

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
        "user": username,
        "room_name": room_name,
    }
    return render(request, 'message.html', context)


def accountscreen(request, room_name="django", username="ibinabo bliss"):
    # Retrieve user and room details from the database
    room_details = db.rooms.find_one({'room_name': room_name})

    if room_details:
        # Update username and room_name if found in the database
        username = room_details.get('username', username)
        room_name = room_details.get('room_name', room_name)

    context = {
        "room_name": room_name,
        "username": username,
    }
    return render(request, 'accounts.html', context)
