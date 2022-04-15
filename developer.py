from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
          self.root=root
          #window size
          self.root.geometry("1920x1080+0+0")
          self.root.title("Face Regonition System")


          title_lbl=Label(self.root,text="DEVELOPER",font=("Times New Roman",30,"bold"),bg="white",fg="blue")
          title_lbl.place(x=0,y=0,width=1300,height=30)


          img_top=Image.open(r"Images\dev.jpg")
          img_top=img_top.resize((1300,610),Image.ANTIALIAS)
          self.photoimg_top=ImageTk.PhotoImage(img_top)

          f_lbl=Label(self.root,image=self.photoimg_top)
          f_lbl.place(x=0,y=30,width=1300,height=610)

          #frame
          main_frame=Frame(f_lbl,bd=2,bg="white")
          main_frame.place(x=700,y=0,width=500,height=500)

          img_top1=Image.open(r"Images\bg1.jpg")
          img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
          self.photoimg_top1=ImageTk.PhotoImage(img_top1)

          f_lbl=Label(main_frame,image=self.photoimg_top1)
          f_lbl.place(x=300,y=0,width=200,height=200)


          #developer info
          dev_label=Label(main_frame,text="Developers:",font=("Times New Roman",17,"bold"),bg="white")
          dev_label.place(x=0,y=5)

          dev_label=Label(main_frame,text="19CE006- Jaineel Bhavsar",font=("Times New Roman",17,"bold"),bg="white")
          dev_label.place(x=0,y=40)
          dev_label=Label(main_frame,text="19CE016 Dhruvil Chaudhary",font=("Times New Roman",17,"bold"),bg="white")
          dev_label.place(x=0,y=80)
          dev_label=Label(main_frame,text="19CE020 Hard Dhruv",font=("Times New Roman",17,"bold"),bg="white")
          dev_label.place(x=0,y=120)
          


          img4=Image.open(r"Images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
          img4=img4.resize((500,300),Image.ANTIALIAS)
          self.photoimg4=ImageTk.PhotoImage(img4)

          f_lbl=Label(main_frame,image=self.photoimg4)
          f_lbl.place(x=0,y=210,width=500,height=300)


















if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()