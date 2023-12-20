import cv2
import numpy as np
import csv
import os
from datetime import datetime
import face_recognition

video_capture = cv2.VideoCapture (0)

ratan_tata= face_recognition.load_image_file("photos/tata.jpeg")
ratan_tata_encoding = face_recognition.face_encodings(ratan_tata)[0]

tesla = face_recognition.load_image_file("photos/tesla.jpeg")
tesla_encoding = face_recognition.face_encodings(tesla)[0]

known_face_encoding = [
ratan_tata_encoding,
tesla_encoding 
]

known_faces_names= [
"Ratan Tata",
"Tesla"
]


students = known_faces_names.copy()

face_locations = []
face_encodings = []
face_names = []
s=True

now = datetime.now()
current_date= now.strftime ("%Y-%m-%d")


with open(current_date + '.csv', 'w+') as f:
    Inwriter = csv.writer(f)
    Inwriter.writerow(['Name','Time'])

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    
    _,frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding,tolerance=0.5)
            name = ""
            face_distance =face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin (face_distance)
            if matches [best_match_index]:
                name = known_faces_names[best_match_index]
                
            face_names.append(name)
            if name in known_faces_names:
                if name in students:
                    students.remove(name)
                    #print (students)
                    print(name)
                    current_time = now.strftime("%H:%M")
                    
                    with open(current_date + '.csv', 'a+') as f:
                        Inwriter = csv.writer(f)
                        Inwriter.writerow([name, current_time])
    cv2.imshow("attendence system", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
