from flask import Flask, render_template, request
import urllib.parse
import json
from roomba import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == "POST":
        
            attempted_password = request.body['password']

            if attempted_password == "beardbeard":
                # Process Command Here
                roomba = Roomba()
                command = request.body['command']
                if command == "start":
                    roomba.start()
                    return "starting the roomba"

                
            else:
                # Incorrect Password
                return "oopsie wrong credentials"

    except Exception as e:
        return "oopsie what happened here?"


if __name__ == "__main__":
    app.run()
