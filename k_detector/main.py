import face_recognition
import paho.mqtt.client as mqtt
import json
import os
import picamera
import numpy as np
from pathlib import Path
from itertools import compress
from greeting_manager import GreetingManager

# Create a GreetingManager
#greeting_manager = GreetingManager(60, "192.168.1.100") # TODO: load host from env?

camera = picamera.PiCamera()
camera.resolution = (320, 240)
small_frame = np.empty((240, 320, 3), dtype=np.uint8)

face_locations = []
face_encodings = []
face_names = []
known_faces = []

root_dir = '.'

for directory, subdirectories, files in os.walk(root_dir):
    for dirs in subdirectories:
        for directory, subdirectories, files in os.walk(dirs):
            for f in files:
                if f.endswith(".jpg" or ".png" or ".jpeg"):
                    face_encoding = face_recognition.face_encodings(face_recognition.load_image_file(root_dir+'/'+dirs+'/'+f))[0]
                    known_faces.append(face_encoding)
                    face_names.append(dirs)

print("training done!")
while True:
    camera.capture(small_frame, format="rgb")

    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    for face_encoding in face_encodings:
        match = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"
        f = list(compress(face_names, match))
        if not f:
            f.append("Unknown")
            print("Unknown face detected")
        else:
            #greeting_manager.greet(f[0])      
            print(f[0])

        print("no faces detected")
