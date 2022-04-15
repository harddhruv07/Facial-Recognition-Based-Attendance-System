from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from datetime import date

today = date.today()
d2 = today.strftime("%B %d, %Y")

mydata=[]

class Attendance:
    def __init__(self,root):
          self.root=root
          #window size
          self.root.geometry("1920x1080+0+0")
          self.root.title("Face Regonition System")
          
          #==========variable==========
          self.var_atten_id=StringVar()
          self.var_atten_roll=StringVar()
          self.var_atten_name=StringVar()
          self.var_atten_dep=StringVar()
          self.var_atten_time=StringVar()
          self.var_atten_date=StringVar()
          self.var_atten_attendance=StringVar()
          

          #window Img1
          img=Image.open(r"Images\smart-attendance.jpg")
          img=img.resize((650,150),Image.ANTIALIAS)
          self.photoimg=ImageTk.PhotoImage(img)

          f_lbl=Label(self.root,image=self.photoimg)
          f_lbl.place(x=0,y=0,width=650,height=150)

          #window Img2
          img2=Image.open(r"Images\iStock-182059956_18390_t12.jpg")
          img2=img2.resize((650,150),Image.ANTIALIAS)
          self.photoimg2=ImageTk.PhotoImage(img2)

          f_lbl=Label(self.root,image=self.photoimg)
          f_lbl.place(x=650,y=0,width=650,height=150)

          #bg Img
          img4=Image.open(r"Images\wp2551980.jpg")
          img4=img4.resize((1300,527),Image.ANTIALIAS)
          self.photoimg4=ImageTk.PhotoImage(img4)

          bg_img=Label(self.root,image=self.photoimg4)
          bg_img.place(x=0,y=130,width=1300,height=527)

          title_lbl=Label(bg_img,text="Attendance Management System",font=("Times New Roman",30,"bold"),bg="white",fg="darkgreen")
          title_lbl.place(x=0,y=0,width=1300,height=30)

          main_frame=Frame(bg_img,bd=2,bg="white")
          main_frame.place(x=10,y=35,width=1250,height=475)
          
          #left frame
          Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("Times New Roman",12,"bold"))
          Left_frame.place(x=10,y=10,width=625,height=525)

          img_left=Image.open(r"Images\face-recognition.png")
          img_left=img_left.resize((615,100),Image.ANTIALIAS)
          self.photoimg_left=ImageTk.PhotoImage(img_left)

          f_lbl=Label(Left_frame,image=self.photoimg_left)
          f_lbl.place(x=5,y=0,width=615,height=100)

          left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
          left_inside_frame.place(x=0,y=105,width=615,height=330)


          #Label and entry
          #attendanceID
          attendanceId_label=Label(left_inside_frame,text="Attendance ID:",font=("Times New Roman",12,"bold"),bg="white")
          attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

          attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("Times New Roman",12,"bold"))
          attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

          #Roll
          rollLabel=Label(left_inside_frame,text="Roll:",font=("comicsansns",11,"bold"),bg="white")
          rollLabel.grid(row=0,column=2,padx=4,pady=8)

          atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font=("comicsansns",11,"bold"))
          atten_roll.grid(row=0,column=3,pady=8)

          #name
          nameLabel=Label(left_inside_frame,text="Name:",font=("comicsansns",11,"bold"),bg="white")
          nameLabel.grid(row=1,column=0)

          atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font=("comicsansns",11,"bold"))
          atten_name.grid(row=1,column=1,pady=8)

          #department
          depLabel=Label(left_inside_frame,text="Department:",font=("comicsansns",11,"bold"),bg="white")
          depLabel.grid(row=1,column=2)

          atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font=("comicsansns",11,"bold"))
          atten_dep.grid(row=1,column=3,pady=8)

          #time
          timeLabel=Label(left_inside_frame,text="Time:",font=("comicsansns",11,"bold"),bg="white")
          timeLabel.grid(row=2,column=0)

          atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font=("comicsansns",11,"bold"))
          atten_time.grid(row=2,column=1,pady=8)

          #date
          dateLabel=Label(left_inside_frame,text="Date:",font=("comicsansns",11,"bold"),bg="white")
          dateLabel.grid(row=2,column=2)

          atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font=("comicsansns",11,"bold"))
          atten_date.grid(row=2,column=3,pady=8)

          #attendance
          attendanceLabel=Label(left_inside_frame,text="Attendance Status",bg="white",font="comicsansns 11 bold")
          attendanceLabel.grid(row=3,column=0)

          self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
          self.atten_status["values"]=("Status","Present","Absent")
          self.atten_status.grid(row=3,column=1,pady=8)
          self.atten_status.current(0)


          #buttonsframe
          btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
          btn_frame.place(x=0,y=275,width=605,height=35)

          import_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=14,font=("Times New Roman",13,"bold"),bg="blue",fg="white")
          import_btn.grid(row=0,column=0)

          export_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=14,font=("Times New Roman",13,"bold"),bg="blue",fg="white")
          export_btn.grid(row=0,column=1)

          update_btn=Button(btn_frame,text="Email",command=self.send_email,width=14,font=("Times New Roman",13,"bold"),bg="blue",fg="white")
          update_btn.grid(row=0,column=2)

          reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("Times New Roman",13,"bold"),bg="blue",fg="white")
          reset_btn.grid(row=0,column=3)

          
          
          #right frame
          Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Times New Roman",12,"bold"))
          Right_frame.place(x=635,y=5,width=605,height=460)

          table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
          table_frame.place(x=5,y=5,width=590,height=410)


          #=============scroll bar==========
          scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
          scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


          self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_y.set)
          
          scroll_x.pack(side=BOTTOM,fill=X)
          scroll_y.pack(side=RIGHT,fill=Y)
          scroll_x.config(command=self.AttendanceReportTable.xview)
          scroll_y.config(command=self.AttendanceReportTable.yview)

          self.AttendanceReportTable.heading("id",text="Attendance ID")
          self.AttendanceReportTable.heading("roll",text="Roll")
          self.AttendanceReportTable.heading("name",text="Name")
          self.AttendanceReportTable.heading("department",text="Department")
          self.AttendanceReportTable.heading("time",text="Time")
          self.AttendanceReportTable.heading("date",text="Date")
          self.AttendanceReportTable.heading("attendance",text="Attendance")

          self.AttendanceReportTable["show"]="headings"
          self.AttendanceReportTable.column("id",width=100)
          self.AttendanceReportTable.column("roll",width=100)
          self.AttendanceReportTable.column("name",width=100)
          self.AttendanceReportTable.column("department",width=100)
          self.AttendanceReportTable.column("time",width=100)
          self.AttendanceReportTable.column("date",width=100)
          self.AttendanceReportTable.column("attendance",width=100)


          self.AttendanceReportTable.pack(fill=BOTH,expand=1)
          self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

     #================fetchdata===========================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #=============Import Csv============================  
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata) 
    #=============export Csv============================  
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported Successfully to "+os.path.basename(fln))
        except  Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)



    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])



    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

    def send_email(self):
        fromaddr = "harddhruv@gmail.com"
        toaddr = "19ce020@charusat.edu.in"
        
        # instance of MIMEMultipart
        msg = MIMEMultipart()
        
        # storing the senders email address  
        msg['From'] = fromaddr
        
        # storing the receivers email address 
        msg['To'] = toaddr
        
        # storing the subject 
        msg['Subject'] = "Attendance Report"
        
        # string to store the body of the mail
        body = "Attendance File of Date: " + d2
        
        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))
        
        # open the file to be sent 
        filename = "attendance.csv"
        attachment = open(r"attendance.csv", "rb")
        
        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')
        
        # To change the payload into encoded form
        p.set_payload((attachment).read())
        
        # encode into base64
        encoders.encode_base64(p)
        
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        
        # attach the instance 'p' to instance 'msg'
        msg.attach(p)
        
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        # start TLS for security
        s.starttls()
        
        # Authentication
        s.login(fromaddr, "Bhargav@0703")
        
        # Converts the Multipart msg into a string
        text = msg.as_string()
        
        # sending the mail
        s.sendmail(fromaddr, toaddr, text)
        
        # terminating the session
        s.quit()

        messagebox.showinfo("Success","Email sent successfully",parent=self.root)

if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
