from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1526x795+0+0")
        self.root.title("Student Details")

        #======================variables=======================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_gen=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()

        #image1
        img1=Image.open(r"C:\15\3-2 IP PROJECT\Images\img1.png")
        img1=img1.resize((508,120))
        self.p_img1=ImageTk.PhotoImage(img1)

        l_img1=Label(self.root,image=self.p_img1)
        l_img1.place(x=0,y=0,width=508,height=120)


        #image2
        img2=Image.open(r"C:\15\3-2 IP PROJECT\Images\img2.jpg")
        img2=img2.resize((508,120))
        self.p_img2=ImageTk.PhotoImage(img2)

        l_img2=Label(self.root,image=self.p_img2)
        l_img2.place(x=508,y=0,width=508,height=120)


        #image 3
        img3=Image.open(r"C:\15\3-2 IP PROJECT\Images\img3.png")
        img3=img3.resize((508,120))
        self.p_img3=ImageTk.PhotoImage(img3)

        l_img3=Label(self.root,image=self.p_img3)
        l_img3.place(x=1016,y=0,width=508,height=120)

        #bg_image
        bg_img=Image.open(r"C:\15\3-2 IP PROJECT\Images\home_bg.webp")
        bg_img=bg_img.resize((1526,675))
        self.p_bg_img=ImageTk.PhotoImage(bg_img)

        l_bg_img=Label(self.root,image=self.p_bg_img)
        l_bg_img.place(x=0,y=120,width=1526,height=675)

        #title on bg_img
        l_title=Label(l_bg_img,text="STUDENT DETAILS",font=("bold",35),bg="black",fg="white")
        l_title.place(x=0,y=0,width=1526,height=50)

        main_frame=Frame(l_bg_img,bd=2,background="white")
        main_frame.place(x=18,y=55,width=1490,height=625)

        #left frame
        left_frame=LabelFrame(main_frame,bd=6,relief=RIDGE,text="Student Details",font=("bold",10,"bold"),foreground="black",background="#3AAFA9")
        left_frame.place(x=10,y=10,width=730,height=600)

        l_img=Image.open(r"C:\15\3-2 IP PROJECT\Images\SD_left_frame.jpg")
        l_img=l_img.resize((718,110))
        self.p_lfi=ImageTk.PhotoImage(l_img)

        lf_l_img=Label(left_frame,image=self.p_lfi)
        lf_l_img.place(x=0,y=0,width=718,height=110)

        #cuurent course
        curr_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Info",font=("bold",10,"bold"))
        curr_course_frame.place(x=5,y=120,width=710,height=130)
        #dep_label
        dep_label=Label(curr_course_frame,text="Department",font=("thin",12))
        dep_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        #dep_combobox
        dep_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_dep,font=("thin",12),width=22,state="readonly")
        dep_combo["values"]=["Select Department","CSE","AIML","AIDS","DS"]
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #course_label
        cour_label=Label(curr_course_frame,text="Section",font=("thin",12))
        cour_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        #course_combobox
        cour_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_course,font=("thin",12),width=22,state="readonly")
        cour_combo["values"]=["Select Section","A","B","C"]
        cour_combo.current(0)
        cour_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #year label
        year_label=Label(curr_course_frame,text="Year",font=("thin",12))
        year_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        #year_combobox
        year_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_year,font=("thin",12),width=22,state="readonly")
        year_combo["values"]=["Select Year","I","II","III","IV"]
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #semester
        sem_label=Label(curr_course_frame,text="Semester",font=("thin",12))
        sem_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)
        #sem_combobox
        sem_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_sem,font=("thin",12),width=22,state="readonly")
        sem_combo["values"]=["Select Semester","I","II"]
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)


        #Student details
        student_det_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Student Details",font=("bold",10,"bold"))
        student_det_frame.place(x=5,y=260,width=710,height=310)

        #studentIdLabel
        stuId_label=Label(student_det_frame,text="Student Id:",font=("thin",12))
        stuId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        #studentidEntry
        stuid_entry=ttk.Entry(student_det_frame,textvariable=self.var_id,width=30)
        stuid_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        
        #studentnameLabel
        stuname_label=Label(student_det_frame,text="Student Name:",font=("thin",12))
        stuname_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        #studentnameEntry
        stuname_entry=ttk.Entry(student_det_frame,textvariable=self.var_name,width=30)
        stuname_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        
        #studentrollLabel
        sturoll_label=Label(student_det_frame,text="Roll No:",font=("thin",12))
        sturoll_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        #studentrollEntry
        sturoll_entry=ttk.Entry(student_det_frame,textvariable=self.var_roll,width=30)
        sturoll_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        
        #studentgenderLabel
        stugender_label=Label(student_det_frame,text="Gender:",font=("thin",12))
        stugender_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)
        #studentgenderEntry
        stugender_entry=ttk.Entry(student_det_frame,textvariable=self.var_gen,width=30)
        stugender_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        
        #studentdobLabel
        studob_label=Label(student_det_frame,text="DOB:",font=("thin",12))
        studob_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        #studentdobEntry
        studob_entry=ttk.Entry(student_det_frame,textvariable=self.var_dob,width=30)
        studob_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        
        #studentemailLabel
        stuemail_label=Label(student_det_frame,text="Email:",font=("thin",12))
        stuemail_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)
        #studentemailEntry
        stuemail_entry=ttk.Entry(student_det_frame,textvariable=self.var_email,width=30)
        stuemail_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        
        #studentphoneLabel
        stuphone_label=Label(student_det_frame,text="Phone:",font=("thin",12))
        stuphone_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        #studentphoneEntry
        stuphone_entry=ttk.Entry(student_det_frame,textvariable=self.var_phone,width=30)
        stuphone_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        
        #studentaddressLabel
        stuaddress_label=Label(student_det_frame,text="Address:",font=("thin",12))
        stuaddress_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)
        #studentaddressEntry
        stuaddress_entry=ttk.Entry(student_det_frame,textvariable=self.var_address,width=30)
        stuaddress_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

        #radio buttons
        self.var_radio=StringVar()

        stu_radio1=ttk.Radiobutton(student_det_frame,variable=self.var_radio,text="Take photo sample",value="yes",cursor="hand2")
        stu_radio1.grid(row=4,column=1)

        stu_radio2=ttk.Radiobutton(student_det_frame,text="No sample",variable=self.var_radio,value="no")
        stu_radio2.grid(row=4,column=3)

        #button frame
        but_frame=Frame(student_det_frame,bd=2,relief=RIDGE)
        but_frame.place(x=0,y=200,width=697,height=60)
        #save
        save_but=Button(but_frame,command=self.add_data,text="save",font=("thin",10),width=43,cursor="hand2")
        save_but.grid(row=0,column=0)

        update_but=Button(but_frame,command=self.update,text="update",font=("thin",10),width=41,cursor="hand2")
        update_but.grid(row=0,column=1)

        delete_but=Button(but_frame,command=self.delete,text="delete",font=("thin",10),width=43,cursor="hand2")
        delete_but.grid(row=1,column=0)

        reset_but=Button(but_frame,command=self.reset,text="reset",font=("thin",10),width=41,cursor="hand2")
        reset_but.grid(row=1,column=1)

        #button frame 2
        but1_frame=Frame(student_det_frame,bd=2,relief=RIDGE)
        but1_frame.place(x=0,y=260,width=697,height=30)

        take_photo_button=Button(but1_frame,command=self.generate_data_set,text="Take Photo Sample",font=("thin",10),width=43,cursor="hand2")
        take_photo_button.grid(row=0,column=0)
  
        update_photo_button=Button(but1_frame,text="Update Photo Sample",font=("thin",10),width=41,cursor="hand2")
        update_photo_button.grid(row=0,column=1)

        
        


        #right frame
        right_frame=LabelFrame(main_frame,bd=6,relief=RIDGE,text="Student Details",font=("bold",10,"bold"),foreground="black",background="light blue")
        right_frame.place(x=750,y=10,width=730,height=600)

        #search system
        sear_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Searh System",font=("bold",10))
        sear_frame.place(x=5,y=30,width=710,height=80)

        sear_label=Label(sear_frame,text="Search By:",font=("thin",12))
        sear_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        sear_combo=ttk.Combobox(sear_frame,width=20,font=("thin",11),state="readonly")
        sear_combo["values"]=["Select","Roll number","Phone Number"]
        sear_combo.current(0)
        sear_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        sear_button=Button(sear_frame,text="Search",font=("times new roman",11,"bold"),width=15,cursor="hand2")
        sear_button.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        viewall_button=Button(sear_frame,text="View All",font=("times new roman",11,"bold"),width=15,cursor="hand2")
        viewall_button.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #table Frame

        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Searh System",font=("bold",10))
        table_frame.place(x=5,y=130,width=710,height=400)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","roll","gender","dob",
                                "email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("sem",text="semester")
        self.student_table.heading("id",text="id")
        self.student_table.heading("name",text="name")
        self.student_table.heading("roll",text="roll")
        self.student_table.heading("gender",text="gender")
        self.student_table.heading("dob",text="dob")
        self.student_table.heading("email",text="email")
        self.student_table.heading("phone",text="phone")
        self.student_table.heading("address",text="address")
        self.student_table.heading("photo",text="photo sample status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cur)
        self.fetchdata()


    def add_data(self):
        if self.var_dep.get() == "Select Department":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            conn = None
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="kaaki#rootsql64",
                    database="studentregistration"
                )
                my_cur = conn.cursor()
                my_cur.execute(
                    "insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_roll.get(),
                        self.var_gen.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio.get()
                    )
                )
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted successfully", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error due to: {str(err)}", parent=self.root)



    #================fetch data ==================
    def fetchdata(self):
        conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="kaaki#rootsql64",
                    database="studentregistration"
                )
        my_cur = conn.cursor()
        my_cur.execute("select * from student")
        data=my_cur.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
        conn.close()
    #=================get cursor==============
    def get_cur(self,event=""):
        cur_focus=self.student_table.focus()
        content=self.student_table.item(cur_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_roll.set(data[6])
        self.var_gen.set(data[7])
        self.var_dob.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_address.set(data[11])
        self.var_radio.set(data[12])
    
    #============update==============
    def update(self):
        if self.var_dep.get() == "Select Department":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            conn=None
            try:
                update=messagebox.askyesno("update","Do You Want To Update",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="kaaki#rootsql64",
                        database="studentregistration"
                    )
                    my_cur = conn.cursor()
                    my_cur.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,roll_no=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,photosample=%s where student_id=%s",(
                                                                                                                                        self.var_dep.get(),
                                                                                                                                        self.var_course.get(),
                                                                                                                                        self.var_year.get(),
                                                                                                                                        self.var_sem.get(),
                                                                                                                                        self.var_name.get(),
                                                                                                                                        self.var_roll.get(),
                                                                                                                                        self.var_gen.get(),
                                                                                                                                        self.var_dob.get(),
                                                                                                                                        self.var_email.get(),
                                                                                                                                        self.var_phone.get(),
                                                                                                                                        self.var_address.get(),
                                                                                                                                        self.var_radio.get(),
                                                                                                                                        self.var_id.get()
                                                                                                                                        ))
                else:
                    if not update:
                        return 
                messagebox.showinfo("success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetchdata()
                conn.close()
                
            except Exception as es:
                messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root)
    
    #======================delete=========================

    def delete(self):
        if self.var_id.get()=="":
            messagebox.showerror("delete error","Student id is required",parent=self.root)
        else:
            conn=None
            try:
                d=messagebox.askyesno("delete","Do You Want To Delete",parent=self.root)
                if d>0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="kaaki#rootsql64",
                        database="studentregistration"
                    )
                    sql="delete from student where student_id=%s"
                    val=(self.var_id.get(),)
                    my_cur = conn.cursor()
                    my_cur.execute(sql,val)
                else:
                    if not d:
                        return
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo("deleted","Student details successfully deleted",parent=self.root)

                    
            except Exception as es:
                messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root)
    
    #================reset button================
    def reset(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course") 
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_gen.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")      
    
    #========generte datasets and take photo samples========

    def generate_data_set(self):
        if self.var_dep.get() == "Select Department":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            conn = None
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="kaaki#rootsql64",
                    database="studentregistration"
                )
                my_cur = conn.cursor()
                
                # Retrieve the student ID based on the current information provided
                my_cur.execute(
                    "SELECT student_id FROM student WHERE dep=%s AND course=%s AND year=%s AND semester=%s AND name=%s AND roll_no=%s AND gender=%s AND dob=%s AND email=%s AND phone=%s AND address=%s AND photosample=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_roll.get(),
                        self.var_gen.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio.get()
                    )
                )
                student = my_cur.fetchone()
                
                if student:
                    student_id = student[0]
                else:
                    # Insert the new student and get the student_id
                    my_cur.execute(
                        "INSERT INTO student (dep, course, year, semester, name, roll_no, gender, dob, email, phone, address, photosample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_name.get(),
                            self.var_roll.get(),
                            self.var_gen.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_radio.get()
                        )
                    )
                    conn.commit()
                    student_id = my_cur.lastrowid

                conn.commit()
                self.fetchdata()
                self.reset()
                conn.close()

                # ============= Load data from OpenCV2 =======================
                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        return img[y:y + h, x:x + w]
                    return None

                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        break

                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = f"data/user.{student_id}.{img_id}.jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or img_id == 100:
                            break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Success", "Data sets loaded successfully")

            except Exception as es:
                if conn:
                    conn.close()
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
