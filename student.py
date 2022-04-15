from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
          self.root=root
          #window size
          self.root.geometry("1920x1080+0+0")
          self.root.title("Face Regonition System")



        #========variables===========
          self.var_dep=StringVar()
          self.var_course=StringVar()
          self.var_year=StringVar()
          self.var_semester=StringVar()
          self.var_std_id=StringVar()
          self.var_std_name=StringVar()
          self.var_div=StringVar()
          self.var_roll=StringVar()
          self.var_gender=StringVar()
          self.var_dob=StringVar()
          self.var_email=StringVar()
          self.var_phone=StringVar()
          self.var_address=StringVar()
          self.var_counsellor=StringVar()

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
          img3=img3.resize((450,130),Image.ANTIALIAS)
          self.photoimg3=ImageTk.PhotoImage(img3)

          f_lbl=Label(self.root,image=self.photoimg3)
          f_lbl.place(x=900,y=0,width=400,height=130)

          #bg Img4
          img4=Image.open(r"Images\wp2551980.jpg")
          img4=img4.resize((1300,527),Image.ANTIALIAS)
          self.photoimg4=ImageTk.PhotoImage(img4)

          bg_img=Label(self.root,image=self.photoimg4)
          bg_img.place(x=0,y=130,width=1300,height=527)

          #title Label
          title_lbl=Label(bg_img,text="Student Management System",font=("Times New Roman",30,"bold"),bg="white",fg="darkgreen")
          title_lbl.place(x=0,y=0,width=1300,height=30)

          #frame
          main_frame=Frame(bg_img,bd=2,bg="white")
          main_frame.place(x=10,y=35,width=1250,height=475)

          #left label frame
          Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Times New Roman",12,"bold"))
          Left_frame.place(x=5,y=5,width=625,height=460)

        
          # img_left=Image.open(r"Images\charusat.jpg")
          # img_left=img_left.resize((615,80),Image.ANTIALIAS)
          # self.photoimg_left=ImageTk.PhotoImage(img_left)

          # f_lbl=Label(Left_frame,image=self.photoimg_left)
          # f_lbl.place(x=5,y=0,width=615,height=80)
          
          #current course
          current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Course Information",font=("Times New Roman",12,"bold"))
          current_course_frame.place(x=5,y=0,width=615,height=100)
          
          #Department

          dep_label=Label(current_course_frame,text="Department:",font=("Times New Roman",12,"bold"),bg="white")
          dep_label.grid(row=0,column=0,padx=10)

        
          dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Times New Roman",12,"bold"),state="readonly",width=20)
          dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
          dep_combo.current(0)
          dep_combo.grid(row=0,column=1,padx=2,pady=5,stick=W)

          #Course

          course_label=Label(current_course_frame,text="Course:",font=("Times New Roman",12,"bold"),bg="white")
          course_label.grid(row=0,column=2,padx=10,sticky=W)

        
          course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Times New Roman",12,"bold"),state="readonly",width=20)
          course_combo["values"]=("Select Course","FE","SE","TE","LE")
          course_combo.current(0)
          course_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)


         #year

          year_label=Label(current_course_frame,text="Year:",font=("Times New Roman",12,"bold"),bg="white")
          year_label.grid(row=1,column=0,padx=10,sticky=W)

        
          year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Times New Roman",12,"bold"),state="readonly",width=20)
          year_combo["values"]=("Select Year","2019-2020","2020-2021","2021-2022")
          year_combo.current(0)
          year_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)


          #Semester

          semester_label=Label(current_course_frame,text="Semester:",font=("Times New Roman",12,"bold"),bg="white")
          semester_label.grid(row=1,column=2,padx=10,sticky=W)

        
          semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Times New Roman",12,"bold"),state="readonly",width=20)
          semester_combo["values"]=("Select Semester","1","2")
          semester_combo.current(0)
          semester_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)

          #Class Student Information
          class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("Times New Roman",12,"bold"))
          class_Student_frame.place(x=5,y=100,width=615,height=330)
          
          #studentID
          studentId_label=Label(class_Student_frame,text="StudentID:",font=("Times New Roman",12,"bold"),bg="white")
          studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

          studentId_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("Times New Roman",12,"bold"))
          studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

          #Student Name
          studentName_label=Label(class_Student_frame,text="Student Name:",font=("Times New Roman",12,"bold"),bg="white")
          studentName_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

          studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=18,font=("Times New Roman",12,"bold"))
          studentName_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

          #class division
          class_div_label=Label(class_Student_frame,text="Class Division:",font=("Times New Roman",12,"bold"),bg="white")
          class_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)


          div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("Times New Roman",12,"bold"),state="readonly",width=18)
          div_combo["values"]=("A","B","C")
          div_combo.current(0)
          div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

          #roll_no
          roll_no_label=Label(class_Student_frame,text="Blood Group:",font=("Times New Roman",12,"bold"),bg="white")
          roll_no_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

          roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=18,font=("Times New Roman",12,"bold"))
          roll_no_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

          #rGender
          gender_label=Label(class_Student_frame,text="Gender:",font=("Times New Roman",12,"bold"),bg="white")
          gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

          

          gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("Times New Roman",12,"bold"),state="readonly",width=18)
          gender_combo["values"]=("Male","Female","Other")
          gender_combo.current(0)
          gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

          #DOB
          dob_label=Label(class_Student_frame,text="DOB:",font=("Times New Roman",12,"bold"),bg="white")
          dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

          dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=18,font=("Times New Roman",12,"bold"))
          dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

          #Email
          email_label=Label(class_Student_frame,text="Email:",font=("Times New Roman",12,"bold"),bg="white")
          email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

          email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("Times New Roman",12,"bold"))
          email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

          #PhoneNo
          phone_label=Label(class_Student_frame,text="Phone No:",font=("Times New Roman",12,"bold"),bg="white")
          phone_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

          phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=18,font=("Times New Roman",12,"bold"))
          phone_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

          #Address
          address_label=Label(class_Student_frame,text="Address:",font=("Times New Roman",12,"bold"),bg="white")
          address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

          address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("Times New Roman",12,"bold"))
          address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

          #Counsellor Name
          counsellor_label=Label(class_Student_frame,text="Counsellor Name:",font=("Times New Roman",12,"bold"),bg="white")
          counsellor_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

          counsellor_entry=ttk.Entry(class_Student_frame,textvariable=self.var_counsellor,width=18,font=("Times New Roman",12,"bold"))
          counsellor_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)


          #radio Buttons
          self.var_radio1=StringVar()
          radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
          radiobtn1.grid(row=6,column=0)

          radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No photo sample",value="No")
          radiobtn2.grid(row=6,column=1)

          #buttonsframe
          btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
          btn_frame.place(x=0,y=200,width=605,height=95)

          save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("Times New Roman",13,"bold"),bg="blue",fg="white")
          save_btn.grid(row=0,column=0)

          update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=("Times New Roman",13,"bold"),bg="blue",fg="white")
          update_btn.grid(row=0,column=1)

          delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("Times New Roman",13,"bold"),bg="blue",fg="white")
          delete_btn.grid(row=0,column=2)

          reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("Times New Roman",13,"bold"),bg="blue",fg="white")
          reset_btn.grid(row=0,column=3)

          #button frame1  
          btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
          btn_frame1.place(x=0,y=235,width=605,height=35)

          take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take a Photo Sample",width=29,font=("Times New Roman",13,"bold"),bg="blue",fg="white")
          take_photo_btn.grid(row=0,column=0)

          update_photo_btn=Button(btn_frame1,text="Update photo Sample",width=29,font=("Times New Roman",13,"bold"),bg="blue",fg="white")
          update_photo_btn.grid(row=0,column=1)


          #right label frame
          Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Times New Roman",12,"bold"))
          Right_frame.place(x=635,y=5,width=605,height=460)

          img_right=Image.open(r"Images\fr.png")
          img_right=img_right.resize((615,80),Image.ANTIALIAS)
          self.photoimg_right=ImageTk.PhotoImage(img_right)

          f_lbl=Label(Right_frame,image=self.photoimg_right)
          f_lbl.place(x=5,y=0,width=615,height=80)

          #===========Search sytem=================
          
          Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Times New Roman",12,"bold"))
          Search_frame.place(x=5,y=85,width=595,height=70)

          search_label=Label(Search_frame,text="Search By:",font=("Times New Roman",8,"bold"),bg="red",fg="white")
          search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

          search_combo=ttk.Combobox(Search_frame,font=("Times New Roman",13,"bold"),state="readonly",width=12)
          search_combo["values"]=("Select","Roll No","Phone no")
          search_combo.current(0)
          search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

          search_entry=ttk.Entry(Search_frame,width=15,font=("Times New Roman",13,"bold"))
          search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

          search_btn=Button(Search_frame,text="Search",width=10,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
          search_btn.grid(row=0,column=3,padx=4)

          showAll_btn=Button(Search_frame,text="Show All",width=10,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
          showAll_btn.grid(row=0,column=4,padx=4)



          #======================table Frame===================
          table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
          table_frame.place(x=5,y=155,width=595,height=275)


          scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
          scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

          self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","counsellor","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

          scroll_x.pack(side=BOTTOM,fill=X)
          scroll_y.pack(side=RIGHT,fill=Y)
          scroll_x.config(command=self.student_table.xview)
          scroll_y.config(command=self.student_table.yview)

          self.student_table.heading("dep",text="Department")
          self.student_table.heading("course",text="Course")
          self.student_table.heading("year",text="Year")
          self.student_table.heading("sem",text="Semester")
          self.student_table.heading("id",text="ID")
          self.student_table.heading("name",text="Name")
          self.student_table.heading("div",text="Division")
          self.student_table.heading("dob",text="DOB")
          self.student_table.heading("email",text="Email")
          self.student_table.heading("phone",text="Phone No")
          self.student_table.heading("address",text="Address")
          self.student_table.heading("counsellor",text="Counsellor")
          self.student_table.heading("photo",text="PhotoSampleStatus")
          self.student_table.heading("roll",text="Roll No")
          self.student_table.heading("gender",text="Gender")
          self.student_table["show"]="headings"

          self.student_table.column("dep",width=100)
          self.student_table.column("course",width=100)
          self.student_table.column("year",width=100)
          self.student_table.column("sem",width=100)
          self.student_table.column("id",width=100)
          self.student_table.column("name",width=100)
          self.student_table.column("roll",width=100)
          self.student_table.column("gender",width=100)
          self.student_table.column("div",width=100)
          self.student_table.column("dob",width=100)
          self.student_table.column("email",width=100)
          self.student_table.column("phone",width=100)
          self.student_table.column("address",width=100)
          self.student_table.column("counsellor",width=100)
          self.student_table.column("photo",width=150)

          self.student_table.pack(fill=BOTH,expand=1)
          self.student_table.bind("<ButtonRelease>",self.get_cursor)
          self.fetch_data()
  
  
  # ======================Function Declaration==============
    def add_data(self):
       if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All fields are required",parent=self.root)
       else:
          try:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_counsellor.get(),self.var_radio1.get()))
         
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Student Detials has been added",parent=self.root)
          except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    #===========fetch data===============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
          self.student_table.delete(*self.student_table.get_children())
          for i in data:
            self.student_table.insert("",END,values=i)
          conn.commit()
        conn.close()
     #==== get function======
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]


        self.var_dep.set(data[0])
        self.var_course.set(data[1]) 
        self.var_year.set(data[2]) 
        self.var_semester.set(data[3]) 
        self.var_std_id.set(data[4]) 
        self.var_std_name.set(data[5]) 
        self.var_div.set(data[6]) 
        self.var_roll.set(data[7]) 
        self.var_gender.set(data[8]) 
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])  
        self.var_address.set(data[12]) 
        self.var_counsellor.set(data[13])
        self.var_radio1.set(data[14])


    #====update function======
    def update_data(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All fields are required",parent=self.root)

      else:
        try:
          Update=messagebox.askyesno("Update","Do you want to update this details?",parent=self.root)
          if Update>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Counsellor=%s,PhotoSample=%s where Student_id=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_counsellor.get(),self.var_radio1.get(),self.var_std_id.get()))
          else:
            if not Update:
              return
          messagebox.showinfo("Success","Student Details successfully updated",parent=self.root)
          conn.commit()
          self.fetch_data()
          conn.close()    
        except Exception as es:
          messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
      
      #=====delete function=======
    def delete_data(self):
        if self.var_std_id.get()=="":
          messagebox.showerror("Error","Student Id must be required",parent=self.root)
        else:
          try:
            delete=messagebox.askyesno("Student Delete page","Do you want to delete this student",parent=self.root)
            if delete>0:
              conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
              my_cursor=conn.cursor()
              sql="delete from student where Student_id=%s"
              val=(self.var_std_id.get(),)
              my_cursor.execute(sql,val)
            else:
              if not delete:
                return
            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
          except Exception as es:
           messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)    
      
      #====reset=======
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_counsellor.set("")
        self.var_radio1.set("")
    
    #generate dataset and take photo sample
    def generate_dataset(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All fields are required",parent=self.root)

      else:
        try:
          conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
          my_cursor=conn.cursor()
          my_cursor.execute("Select * from student")
          myresult=my_cursor.fetchall()
          id=0
          for x in myresult:
            id+=1
          my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Counsellor=%s,PhotoSample=%s where Student_id=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_counsellor.get(),self.var_radio1.get(),self.var_std_id.get()==id+1))
          conn.commit()
          self.fetch_data()
          self.reset_data()
          conn.close()

          #load predefined data on face frontals from opencv
          detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


          # def face_cropped(img):
          #   gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
          #   faces=face_classifier.detectMultiScale(gray,1.3,5)#scaling factor=1.3 & Minimum Neighbour=5
          #   for(x,y,w,h) in faces:
          #     face_cropped=img[y:y+h,x:x+w]
          #     return face_cropped


          cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)#to on the camera
          sampleNum = 0

          while True:
            ret,img=cap.read()
            
            # if face_cropped(my_frame) is not None:
            #   img_id+=1
            #   face=cv2.resize(face_cropped(my_frame),(450,450))
            #   face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

            #   file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg" #to save images captured by camera in folder data
            #   cv2.imwrite(file_name_path,face)
            #   cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
            #   cv2.imshow("Cropped Face",face)


            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)

            for (x, y, w, h) in faces:
              cv2.rectangle(img, (x, y), (x + w, y + h), (10,159,255), 2)
              sampleNum = sampleNum+1
            
              file_name_path="data/user."+str(id)+"."+str(sampleNum)+".jpg" #to save images captured by camera in folder data

              cv2.imwrite(file_name_path,gray[y:y+h, x:x+w])
            # cv2.putText(img,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
            cv2.imshow("Cropped Face",img)


            # if cv2.waitKey(1)==13 or int(img_id)==100:
            #   break

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            
            elif sampleNum > 100:
                break
          cap.release()
          cv2.destroyAllWindows()
          messagebox.showinfo("Result","Generating datasets completed",parent=self.root)

        except Exception as es:
          messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  

           






        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
