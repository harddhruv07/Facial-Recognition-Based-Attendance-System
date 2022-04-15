from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
          self.root=root
          #window size
          self.root.geometry("1920x1080+0+0")
          self.root.title("Face Regonition System")


          title_lbl=Label(self.root,text="Train Data Set",font=("Times New Roman",30,"bold"),bg="white",fg="red")
          title_lbl.place(x=0,y=0,width=1300,height=30)


          img_top=Image.open(r"Images\facialrecognition.png")
          img_top=img_top.resize((1300,300),Image.ANTIALIAS)
          self.photoimg_top=ImageTk.PhotoImage(img_top)

          f_lbl=Label(self.root,image=self.photoimg_top)
          f_lbl.place(x=0,y=40,width=1300,height=300)

          #button
          b2=Button(self.root,text="Train Data",cursor="hand2",command=self.train_classifier,font=("Times New Roman",25,"bold"),bg="red",fg="white")
          b2.place(x=0,y=340,width=1300,height=30)
          

          img_bottom=Image.open(r"Images\dev.jpg")
          img_bottom=img_bottom.resize((1300,300),Image.ANTIALIAS)
          self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

          f_lbl=Label(self.root,image=self.photoimg_bottom)
          f_lbl.place(x=0,y=370,width=1300,height=300)
    
    def train_classifier(self):
        data_dir=("data")
        path=[ os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)#88% performance to convert array


        #===Train Classiefier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows
        messagebox.showinfo("Result","Training Datasets Completed",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()          