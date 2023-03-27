import base64
import random
from flask import Flask,request
from flask_socketio import SocketIO,emit,send
from model import load_corpus, check_similarity,get_feedback
from dataset import salutations, salutation_feedback,salutations1, salutation_feedback1
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = "Amazinganalysisbot"
socketio = SocketIO(app, cors_allowed_origins='*')


#a dictionary to store logged in users
#key for username, random_session id as value

users  = {}

#on connect function
@socketio.on('connect')
def on_connect(socket):
    load_corpus()
    print("Connected")
    pass

#saves the users who have connected by saving username and session_id in the user's dictionary
@socketio.on('connection')
def save_session(payload):

    sesssion_id    = request.sid
    username = payload['username']

    #save the username and session_id in the user's dictionary
    try:
        
        users[username]  = sesssion_id
        #payload = {"message" : "I'm CPIMS user friendly chatbot, currently I'm currently offline for active development.I'll be back soon."}
        
        #emit("initialResponse",  payload, room=sesssion_id)
    
    except Exception as e:
        if e.__class__.__name__  == 'KeyError':
            pass
#sending an image or images 

@socketio.on('visualization')
def image():

    with open('1.png', mode='rb') as f:
        image_data  = f.read()

    #encode the image data as base64
    encoded_image = base64.b64encode(image_data)

    #send the encode image through socketio
    socketio.emit("visulization", {'image': encoded_image.decode('utf-8')})

#works on user messages, taking them in, processing and replying them in real time
@socketio.on('message')
def message(payload):
    #starttime = time.perf_counter()
    #take in user message, and username
    user_message = payload['message']
    user_name  = payload['username']
    if user_message.lower().strip() in salutations:
        random_salutation = random.choice(salutation_feedback)
        emit("message", {"message": random_salutation}, room=users[user_name])

    elif user_message.lower().strip() in salutations1:
        random_salutation = random.choice(salutation_feedback1)
        emit("message", {"message": random_salutation}, room=users[user_name])

    else:
        try:
            check_similarity(user_message)
            feedback = get_feedback()

            emit("message", {"message": feedback}, room=users[user_name])

        except Exception as e:
            if e.__class__.__name__ == 'KeyError':
                pass
            else:
                print("error")
    

#takes note of users who have been disconnected.....a bit useless here
@socketio.on('disconnect')
def on_disconnect():
    print(f"user with session id {request.sid} disconnected")
    #possibly get  a disconnected user

    pass

if __name__ == "__main__":

    socketio.run(app,debug=True, port=3000)

