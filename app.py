from flask import Flask, request, session
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from bob import ask, append_interaction_to_chat_log


app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')

    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                         chat_log)

    response = MessagingResponse()
    message = Message()
    message.body(answer)
    response.append(message)
    print(response)
    return str(response)