import os

from dotenv import load_dotenv
from flask import (
    Flask,
    flash, 
    render_template, 
    redirect,
    request,
    url_for,
)
from twilio.rest import Client
from pymongo import MongoClient

load_dotenv()
app = Flask(__name__)

TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')

client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)

def get_sent_messages():
    messages = client.messages.list(from_=TWILIO_PHONE_NUMBER)
    return messages

def send_message(to, body):
    client.messages.create (
      to = to,
      body = body,
      from_=TWILIO_PHONE_NUMBER 
    )

    mongourl = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@mongo:27017/"
    try:
        mycli = MongoClient(mongourl)
    except:
        print("Error Connecting to DataBase")
        exit(1)

    mydb = mycli["Compliment01"]
    mycol = mydb["from-15177779020"]
    mydict = {"to":to, "from":TWILIO_PHONE_NUMBER, "body":body}
    mycol.insert_one(mydict)

@app.route("/", methods=["GET"])
def index():
    messages = get_sent_messages()
    return render_template("index.html", messages=messages)

@app.route("/add-compliment", methods=["POST"])
def add_compliment():
    sender = request.values.get('sender', 'Someone')
    receiver = request.values.get('receiver', 'Someone')
    compliment = request.values.get('compliment', 'wonderful')
    to = request.values.get('to')
    body = f'{sender} says: {receiver} is {compliment}. See more compliments at {request.url_root}'
    send_message(to, body)
    flash('Your message was successfully sent')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
