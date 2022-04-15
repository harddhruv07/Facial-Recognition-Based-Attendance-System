from cProfile import label
from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import font
import tkinter
from main import Face_Recognition_System
from time import strftime
from datetime import datetime
from turtle import width
from help import Help
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1920x1080+0+0")


        self.bg=ImageTk.PhotoImage(file=r"images\un.jpg")#bg image path

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=140,width=260,height=350)

        img1=Image.open(r"images/LoginIconAppl.png")#frame image path
        img1=img1.resize((70,70),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=590,y=140,width=80,height=80)

        get_str=Label(frame,text="Get Started",font=("times new roman",15,"bold"),fg="white",bg="black")
        get_str.place(x=75,y=76)


        #label
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=40,y=105)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=20,y=135,width=230)


        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=40,y=170)

        self.txtpass=ttk.Entry(frame,show='*',font=("times new roman",15,"bold"))
        self.txtpass.place(x=20,y=203,width=230)



        #================Icon Images=======================
        img2=Image.open(r"images/LoginIconAppl.png")#user icon image path
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg1.place(x=515,y=248,width=25,height=25)


        img3=Image.open(r"images/lock-512.png")#pass icon image path
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg1.place(x=515,y=314,width=25,height=25)


        #========login Button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=70,y=240,width=120,height=30)

        #========Register Button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=285,width=120,height=30)

        #========Forgot Password Button
        forgotbtn=Button(frame,text="Forgot Password?",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=10,y=305,width=120,height=30)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Are Required")  
        elif self.txtuser.get()=="User" and self.txtpass.get()=="pass":
            messagebox.showinfo("Success","Welcome to Attendance System")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(self.txtuser.get(),self.txtpass.get()))

            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()        

    # ========reset password========

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter the Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been Reset, Please Login with new Password",parent=self.root2)
                self.root2.destroy()




    # ==========forget password========

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email Address to Reset Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("My Error","Please Enter the Valid Name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x400+550+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",15,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=45,y=50)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Birth Date","Your Pet Name")
                self.combo_security_Q.place(x=45,y=85,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=45,y=125)
        
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=45,y=160,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=45,y=200)
        
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=45,y=235,width=250)

                btn=Button(self.root2,command=self.reset_pass,text="Reset",font=("times new roman",15,"bold"),bg="green",fg="white")
                btn.place(x=75,y=275)



#====================Register============================
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1920x1080+0+0")


        #==============variables==========================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #bg img
        self.bg=ImageTk.PhotoImage(file=r"images/u.jpg")
        #label
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #left img
        self.bg1=ImageTk.PhotoImage(file=r"images/thought-good-morning-messages-LoveSove.jpg")
        #label
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=70,y=50,width=370,height=550)

        #mainframe
        frame=Frame(self.root,bg="white")
        frame.place(x=440,y=50,width=700,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",15,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=15,y=15)


        #labels and entry
        fname=Label(frame,text="First Name",font=("times new roman",12,"bold"),bg="white")
        fname.place(x=45,y=60)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",12,"bold"))
        fname_entry.place(x=45,y=85,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",12,"bold"),bg="white",fg="black")
        lname.place(x=350,y=60)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",12))
        self.txt_lname.place(x=350,y=85,width=250)
        
        contact=Label(frame,text="Contact No.",font=("times new roman",12,"bold"),bg="white",fg="black")
        contact.place(x=45,y=130)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",12))
        self.txt_contact.place(x=45,y=155,width=250)

        email=Label(frame,text="Email",font=("times new roman",12,"bold"),bg="white",fg="black")
        email.place(x=350,y=130)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",12))
        self.txt_email.place(x=350,y=155,width=250)

        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=45,y=200)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Birth Date","Your Pet Name")
        self.combo_security_Q.place(x=50,y=230,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=350,y=200)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=350,y=230,width=250)


        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=45,y=272)

        self.txt_pswd=ttk.Entry(frame,show='*',textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=45,y=300,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=350,y=270)

        self.txt_confirm_pswd=ttk.Entry(frame,show='*',textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=350,y=300,width=250)


        #check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=40,y=340)


        #buttons
        img=Image.open(r"images/register-now-button1.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=35,y=375,width=200)



        img1=Image.open(r"images/loginpng.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=340,y=375,width=200)
    

    #========================Function Declaration========================================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same ")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree To Terms & Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already Registered")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_securityQ.get(),self.var_securityA.get(),self.var_pass.get()))                
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")

    def return_login(self):
        self.root.destroy()

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


if __name__ =="__main__":
    main()
