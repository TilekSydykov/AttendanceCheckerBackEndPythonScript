#!/usr/bin/env python3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import pyrebase
from datetime import datetime

print("all libraries imported")

config = {
  "apiKey": "secret",
  "authDomain": "fireprint-c310b.firebaseapp.com",
  "databaseURL": "https://fireprint-c310b.firebaseio.com",
  "storageBucket": "fireprint-c310b.appspot.com"
}

firebase = pyrebase.initialize_app(config)

reader = SimpleMFRC522()

last_uid = 0

checker_id = "kS7Nf"

run = True

print("all staff created")

def wait_read():
    ide = 0
    text = 0
    try:
        ide, text = reader.read()
    except:
        print("Error")
    finally:
        text = 1
        print(ide)
    return ide

def sent_to_internet(uid):
    last_uid = uid
    db = firebase.database()
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    timestamp 
    data = {"user": uid, "time": timestamp}
    db.child("checks").child(checker_id).push(data)

print("main loop begin")
while run:
    ide = wait_read()
    if not last_uid == ide:
        sent_to_internet(ide)
        print("send")
    last_uid = ide
    time.sleep(1)

GPIO.cleanup()
