from flask import Flask
from flask_ask import Ask, statement, question
import time
import logging
from os import system

app = Flask(__name__)
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def start_skill():
    welcome_message = 'All systems good. What mode are we doing?'
    return question(welcome_message)

@ask.intent("LaneKeepIntent")
def lane_keeping():
    system("roslaunch lane_follower lane_follower_bag.launch")
    return statement("Launching Lane Keeping.")

@ask.intent("MappingIntent")
def mapping():
    system("roslaunch lane_follower hector_slam_test.launch")
    return statement("Launching mapping with hector slam.")
    
if __name__ == '__main__':
    app.run(debug=True)
