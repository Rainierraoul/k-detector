import face_recognition
#import cv2
import paho.mqtt.client as mqtt
import json
import os
import picamera
from pathlib import Path
from itertools import compress
from greeting_manager import GreetingManager

# Create a GreetingManager
greeting_manager = GreetingManager(60, "192.168.0.102") # TODO: load host from env?

#video_capture = cv2.VideoCapture(0)
camera = picamera.PiCamera()
camera.resolution = (320, 240)
small_frame = np.empty((240, 320, 3), dtype=np.uint8)

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
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

while True:
    #ret, frame = video_capture.read()
    #small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    camera.capture(small_frame, format="rgb")

    if process_this_frame:
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        for face_encoding in face_encodings:
            match = face_recognition.compare_faces(known_faces, face_encoding)
            name = "Unknown"
            f = list(compress(face_names, match))
            if not f:
                f.append("Unknown")
            else:
                greeting_manager.greet(f[0])      
    process_this_frame = not process_this_frame
    
    '''
    for (top, right, bottom, left), name in zip(face_locations, f):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()'''