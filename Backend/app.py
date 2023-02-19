import random
from flask import Flask,request
from flask_socketio import SocketIO,emit,send
from model import load_dataset, process
from dataset import salutations, salutation_feedback,salutations1, salutation_feedback1,malaria_commands
from decode import data,predict,total,allocation


app = Flask(__name__)
app.config['SECRET_KEY'] = "MEHNTHISSHITSUCKS"
socketio = SocketIO(app, cors_allowed_origins='*')


#a dictionary to store logged in users
#key for username, random_session id as value

users  = {}

#on connect function
@socketio.on('connect')
def on_connect(socket):
    load_dataset()
    #print("Connected")
    pass


#saves the users who have connected by saving username and session_id in the user's dictionary
@socketio.on('connection')
def save_session(payload):

    sesssion_id    = request.sid
    username = payload['username']

    #save the username and session_id in the user's dictionary
    try:
        
        users[username]  = sesssion_id
        
        #emit("initialResponse",  payload, room=sesssion_id)
    
    except Exception as e:
        if e.__class__.__name__  == 'KeyError':
            pass

#works on user messages, taking them in, processing and replying them in real time
@socketio.on('message')
def message(payload):
    #take in user message, and username
    user_message = payload['message']
    
    message = user_message.lower().strip()
    user_name  = payload['username']
    if user_message.lower().strip() in salutations:
        random_salutation = random.choice(salutation_feedback)
        emit("message", {"message": random_salutation}, room=users[user_name])
    elif user_message == 'Why a chatbot':
        emit("message",{"message" :"A chatbot can be used in data analysis to provide quick access to insights and trends, answer questions about data, and guide users through data visualization and exploration, improving efficiency and enabling better decision-making."}, room=users[user_name])
    elif user_message == 'commands':
        emit("message", {"message": "some of my commands for you to find the insight of data are: 'predict for (enter_no_of_years) years', 'data shape' to get shape, 'data column' to get columns and many more." }, room=users[user_name])
    elif user_message.lower().strip() in salutations1:
        random_salutation = random.choice(salutation_feedback1)
        emit("message", {"message": random_salutation}, room=users[user_name])
        
    elif message[:12] in malaria_commands:
        emit("message", {"message": "I'm sorry but the model to get distribution of values is not working."}, room=users[user_name])
    elif message[:10] in malaria_commands:
        feedback = allocation(message)
        emit("message", {"message": feedback}, room=users[user_name])
    elif message[:5] in malaria_commands:
        feedback = total(message)
        
        emit("message", {"message": feedback}, room=users[user_name])
    elif message[:7] in malaria_commands:
        feedback = predict(message)
        emit("message", {"message": feedback}, room=users[user_name])

    elif message[:4] in malaria_commands:
        feedback = data(message)
        emit("message", {"message": feedback}, room=users[user_name])

    else:
        try:
            feedback  = process(user_message)

            #print(feedback)

            emit("message", {"message": feedback}, room=users[user_name])

        except Exception as e:
            if e.__class__.__name__ == 'KeyError':
                pass
    

#takes note of users who have been disconnected.....a bit useless here
@socketio.on('disconnect')
def on_disconnect():
    print(f"user with session id {request.sid} disconnected")
    #possibly get  a disconnected user

    pass

if __name__ == "__main__":

    socketio.run(app,debug=True, port=3000)

