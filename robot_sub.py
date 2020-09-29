from flask import Flask
from flask_ask import Ask, statement, question
import time
import logging
from os import system
import subprocess



app = Flask(__name__)
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def start_skill():
    subprocess.Popen(["roslaunch", "lane_follower", "robot_initialize.launch"])
    time.sleep(5)
    welcome_message = 'All systems good. What would you like to do?'
    return question(welcome_message)

@ask.intent("LaneKeepIntent")
def lane_keeping():
    subprocess.Popen(["roslaunch", "lane_follower", "lane_follower.launch"])
    return statement("Launching Lane Keeping.")

@ask.intent("MappingIntent")
def mapping():
    subprocess.Popen(["roslaunch", "lane_follower", "hector_slam_test.launch"])
    return statement("Launching mapping with hector slam.")
    
@ask.intent("KillIntent")
def kill_ros():
    system("killall -9 rosmaster")
    return statement("Killing all nodes now.")

if __name__ == '__main__':
    app.run(debug=True)
