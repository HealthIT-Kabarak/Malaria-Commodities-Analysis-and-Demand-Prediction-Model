import os
"""elif user_message == 'Why a chatbot':
        emit("message",{"message" :"A chatbot can be used in data analysis to provide quick access to insights and trends, answer questions about data, and guide users through data visualization and exploration, improving efficiency and enabling better decision-making."}, room=users[user_name])
    elif user_message == 'commands':
        emit("message", {"message": "some of my commands for you to find the insight of data are: \n 'predict for (enter_no_of_years) years', 'data shape' to get shape, 'data column' to get columns and many more." }, room=users[user_name])
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
        emit("message", {"message": feedback}, room=users[user_name])"""


import itertools

data   = [1,2,3,4,5,6,7,8,9,10,11,12]

data2 = ["name", "army","worm","cooper","retard", "pry", "science","man", "protege", "forth"]


data3 = ['gregory isaacs', 'bob marley', 'siddy ranks', 'israel vibration', 'ub40', 'lucky dube', 'bnny wailer']


for n,k,v in itertools.zip_longest(data,data2,data3):
    if v is not None:
        print(n,k,v)

    else:

        print(n,k,v)



