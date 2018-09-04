import cv2
from tkinter import *
import serial
import struct
#conexao = serial.Serial("COM3",9600);

cap = cv2.VideoCapture(0)

def umaface():
    for (x,y,w,h) in faces:
            resul=(((x+x+w)/2)*180)/640
            resul2=(((y+y+h)/2)*180)/480
            if(resul>85 and resul<95 and resul2>85 and resul2 <95):
             cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
             roi_gray = gray[y:y+h, x:x+w]
             roi_color = frame[y:y+h, x:x+w]                       
            else:
             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
             roi_gray = gray[y:y+h, x:x+w]
             roi_color = frame[y:y+h, x:x+w]    
             for (x,y,w,h) in facelado:
                resul=(((x+x+w)/2)*180)/640
                resul2=(((y+y+h)/2)*180)/480
                if(resul>85 and resul<95 and resul2>85 and resul2 <95):
                 cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                 roi_gray = gray[y:y+h, x:x+w]
                 roi_color = frame[y:y+h, x:x+w]                       
                else:
                 cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                 roi_gray = gray[y:y+h, x:x+w]
                 roi_color = frame[y:y+h, x:x+w]    
def duasface():

    for (x,y,w,h) in faces:
         resul=(((x+x+w)/2)*180)/640         
         if(resul<=90):
             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
             roi_gray = gray[y:y+h, x:x+w]
             roi_color = frame[y:y+h, x:x+w]                         
             print("faço a conta")
         else:
             cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
             roi_gray = gray[y:y+h, x:x+w]
             roi_color = frame[y:y+h, x:x+w]            
             print("não faço a conta")            
             for (x,y,w,h) in facelado:
              resul=(((x+x+w)/2)*180)/640         
              if(resul<=90):
                 cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                 roi_gray = gray[y:y+h, x:x+w]
                 roi_color = frame[y:y+h, x:x+w]                         
                 print("faço a conta")
              else:
                 cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                 roi_gray = gray[y:y+h, x:x+w]
                 roi_color = frame[y:y+h, x:x+w]            
                 print("não faço a conta")            

face_cascades =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade =cv2.CascadeClassifier('haarcascade_profileface.xml')
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(gray, 1.2, 5)
    facelado = face_cascade.detectMultiScale(gray, 1.2, 5)

    if(len(faces)>1):
        duasface()           
    else:        
        umaface()             
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
