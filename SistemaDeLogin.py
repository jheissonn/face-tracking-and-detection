from tkinter import*
from tkinter import messagebox
import serial
import struct
import cv2


janela=Tk()



def bt_click():
 
   if ((str(Login.get())== ("admin")) &( str(Senha.get())==("admin")) ):
        
      cap = cv2.VideoCapture(0)
      face_cascades =cv2.CascadeClassifier('C:\\Users\\SALA\\Downloads\\teste de gestudo\\haarcascade_frontalface_default.xml')
      face_cascade =cv2.CascadeClassifier('C:\\Users\\SALA\\Downloads\\grupodeestudopronto\\opencv-master\\data\\haarcascades_cuda\\haarcascade_profileface.xml')
      while(True):
    
        ret, frame = cap.read()
        frame = cv2.flip(frame,1)   
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascades.detectMultiScale(gray, 1.3, 5)
        facelado = face_cascade.detectMultiScale(gray, 1.3, 5)
                          
        if(len(faces)>1):        
       
           maisdeuma()     
        else:
            umaface()
          
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cap.release()
        cv2.destroyAllWindows()

   else:
       messagebox.showinfo("ERRO","Login ou senha incorretos")
       
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

def maisdeuma():
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
images=PhotoImage(file="evinci.png")
limage=Label(janela,width=900,height=600,image=images)
limage.place(x=0,y=0)
llogin=Label(janela,text="Informe o login: ",bg='royalblue2')
llogin.place(x=300,y=200)
Login=Entry(janela)
Login.place(x=400,y=200)


lsenha=Label(janela,text="Informe a Senha:",bg='royalblue2')
lsenha.place(x=300,y=230)
Senha=Entry(janela,show="*")
Senha.place(x=400,y=230)


bt=Button(janela,text="Conectar",width=16,fg='white', bg='blue2',
activebackground='black',command=bt_click)
bt.place(x=400,y=260)

janela.geometry("900x600+200+200")
janela.mainloop()
