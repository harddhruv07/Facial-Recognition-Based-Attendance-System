from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
          self.root=root
          #window size
          self.root.geometry("1920x1080+0+0")
          self.root.title("Face Regonition System")

          title_lbl=Label(self.root,text="Face Recognition",font=("Times New Roman",20,"bold"),bg="white",fg="green")
          title_lbl.place(x=0,y=0,width=1300,height=40)
          
          #img1
          img_top=Image.open(r"Images\face_detector1.jpg")
          img_top=img_top.resize((650,590),Image.ANTIALIAS)
          self.photoimg_top=ImageTk.PhotoImage(img_top)

          f_lbl=Label(self.root,image=self.photoimg_top)
          f_lbl.place(x=0,y=40,width=650,height=590)

          #img2
          img_bottom=Image.open(r"Images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
          img_bottom=img_bottom.resize((650,590),Image.ANTIALIAS)
          self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

          f_lbl=Label(self.root,image=self.photoimg_bottom)
          f_lbl.place(x=650,y=40,width=650,height=590)


          b2=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("Times New Roman",15,"bold"),bg="darkgreen",fg="white")
          b2.place(x=250,y=520,width=150,height=40)

    #===================attendance=========================
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")






    #========================Face recognition============================================
    def face_recog(self):

        recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
        recognizer.read("classifier.xml")
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)
        
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        

        while True:
            ret,img =cap.read()
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray, 1.3,5)
            for(x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                id, predict = recognizer.predict(gray[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))
                    
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()


                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence > 77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Blood Group:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)                  
                  
            
            cv2.imshow('image',img) 
            if (cv2.waitKey(1)==ord('q')):
                break


        cap.release()
        cv2.destroyAllWindows()




        # def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
        #     gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #     features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)


        #     coord=[]

        #     for(x,y,w,h) in features:
        #         cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        #         id,predict=clf.predict(gray_image[y:y+h,x:x+w])
        #         confidence=int((100*(1-predict/300)))

                # conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
                # my_cursor=conn.cursor()


                # my_cursor.execute("select Name from student where Student_id="+str(id))
                # n=my_cursor.fetchone()
                # n="+".join(n)

                # my_cursor.execute("select Roll from student where Student_id="+str(id))
                # r=my_cursor.fetchone()
                # r="+".join(r)

                # my_cursor.execute("select Dep from student where Student_id="+str(id))
                # d=my_cursor.fetchone()
                # d="+".join(d)

                # my_cursor.execute("select Student_id from student where Student_id="+str(id))
                # i=my_cursor.fetchone()
                # i="+".join(i)

        #         if confidence>77:
        #             # cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    # cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    # cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    # cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #             # self.mark_attendance(i,r,n,d)
        #         else:
                    # cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    # cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)  

        #         coord=[x,y,w,h]

        #     return coord   


        # def recognize(img,clf,faceCascade):
        #     coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
        #     return img

        # faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
        # clf=cv2.face.LBPHFaceRecognizer_create()
        # clf.read("classifier.xml")

        # video_cap=cv2.VideoCapture(0)


        # while True:
        #     ret,img=video_cap.read()
        #     img=recognize(img,clf,faceCascade)
        #     cv2.imshow("Welcome To Face Recognition",img)

        #     if cv2.waitKey(1)==13:
        #         break
        #     video_cap.release()
        #     cv2.destroyAllWindows()

    

        



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()    