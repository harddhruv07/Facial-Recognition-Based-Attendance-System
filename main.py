from tkinter import*
from tkinter import ttk
from tkinter import font
import tkinter
from time import strftime
from datetime import datetime
from turtle import width
from PIL import Image,ImageTk
from help import Help
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os




class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        #window size
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Regonition System")

        #window Img1
        img=Image.open(r"Images\charusat.jpg")
        img=img.resize((450,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=130)

        #window Img2
        img2=Image.open(r"Images\charusat1.png")
        img2=img2.resize((450,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=400,y=0,width=450,height=130)

        #window Img3
        img3=Image.open(r"Images\charusat.jpg")
        img3=img3.resize((400,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=900,y=0,width=400,height=130)


        #bg Img4
        img4=Image.open(r"Images\bg2.png")
        img4=img4.resize((1300,527),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1300,height=527)

        #title Label
        title_lbl=Label(bg_img,text="Face Regonition Attendance System",font=("Times New Roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=30)
        
        
        #Time
        def time():
                string=strftime('%H:%M:%S %p')
                lbl.config(text=string)
                lbl.after(1000,time)

        lbl=Label(title_lbl,font=("Times New Roman",14,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=30)
        time()

        #Student Button
       
        img5=Image.open(r"Images\gettyimages-1022573162.jpg")
        img5=img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        #button 1
        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=75,width=180,height=140)

        #button 2
        b2=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Times New Roman",12,"bold"),bg="darkblue",fg="white")
        b2.place(x=200,y=215,width=180,height=30)


        #detect face Button
        img6=Image.open(r"Images\face_detector1.jpg")
        img6=img6.resize((180,140),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        #button 1
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=450,y=75,width=180,height=140)

        #button 2
        b2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=450,y=215,width=180,height=30)




        #Attendance Button
        img7=Image.open(r"Images\report.jpg")
        img7=img7.resize((180,140),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        #button 1
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=75,width=180,height=140)

        #button 2
        b2=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=700,y=215,width=180,height=30)


        #help Button
        img8=Image.open(r"Images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img8=img8.resize((180,140),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        #button 1
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help)
        b1.place(x=950,y=75,width=180,height=140)

        #button 2
        b2=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help,font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=950,y=215,width=180,height=30)



        #train Button
        img9=Image.open(r"Images\Train.jpg")
        img9=img9.resize((180,140),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        #button 1
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=270,width=180,height=140)

        #button 2
        b2=Button(bg_img,text="Train DataSet",cursor="hand2",command=self.train_data,font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=200,y=410,width=180,height=30)


        #photos Button
        img10=Image.open(r"Images\facial_recognition_action.jpg")
        img10=img10.resize((180,140),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        #button 1
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=450,y=270,width=180,height=140)

        #button 2
        b2=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=450,y=410,width=180,height=30)



        #Developer Button
        img11=Image.open(r"Images\Team-Management-Software-Development.jpg")
        img11=img11.resize((180,140),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        #button 1
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=270,width=180,height=140)

        #button 2
        b2=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=700,y=410,width=180,height=30)


        #Exit  Button
        img12=Image.open(r"Images\exit.jpg")
        img12=img12.resize((180,140),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        #button 1
        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.IExit)
        b1.place(x=950,y=270,width=180,height=140)

        #button 2
        b2=Button(bg_img,text="Exit",cursor="hand2",command=self.IExit,font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=950,y=410,width=180,height=30)

    def open_img(self):
        os.startfile("data")    

    def IExit(self):
            self.IExit=tkinter.messagebox.askyesno("Face Recognition System","Are you sure you want to exit?",parent=self.root)
            if self.IExit>0:
                self.root.destroy()
            else:
                return 

        #function buttons
    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)


    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)   
        
    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window) 

    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)  

        
    def developer_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Developer(self.new_window)

    def help(self):
            self.new_window=Toplevel(self.root)
            self.app=Help(self.new_window)

        




        


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
