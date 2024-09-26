from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from Student import Student
from tkinter import messagebox
import os
import numpy as np
import cv2
from face_dectector import Face_detector
from attendance import Attendance

class facerecognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1526x795+0+0")
        self.root.title("face recognition")

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
        bg_img=Image.open(r"C:\15\3-2 IP PROJECT\Images\home_bg2.jpg!sw800")
        bg_img=bg_img.resize((1526,675))
        self.p_bg_img=ImageTk.PhotoImage(bg_img)

        l_bg_img=Label(self.root,image=self.p_bg_img)
        l_bg_img.place(x=0,y=120,width=1526,height=675)

        #title on bg_img
        l_title=Label(l_bg_img,text="SMART STUDENT ATTENDANCE",font=("Helvetica", 35, "bold"),bg="black",fg="white")
        l_title.place(x=0,y=0,width=1526,height=50)

        #1st button
        first_button=Image.open(r"C:\15\3-2 IP PROJECT\Images\student_details.jpg")
        first_button=first_button.resize((250,350))
        self.p_first_image=ImageTk.PhotoImage(first_button)

        l_first_button=Button(l_bg_img,image=self.p_first_image,cursor="hand2",command=self.stu_detail_button)
        l_first_button.place(x=80,y=130,width=250,height=350)

        f_button=Button(l_bg_img,text="student details",command=self.stu_detail_button,font=("bold",15),fg="white",bg="blue",activebackground="blue",cursor="hand2")
        f_button.place(x=80,y=480,width=250,height=30)

        #2nd button
        second_button=Image.open(r"C:\15\3-2 IP PROJECT\Images\face_recognition.png")
        second_button=second_button.resize((250,350))
        self.p_second_image=ImageTk.PhotoImage(second_button)

        l_second_button=Button(l_bg_img,image=self.p_second_image,cursor="hand2")
        l_second_button.place(x=410,y=130,width=250,height=350)

        f_button=Button(l_bg_img,command=self.face_detector,text="Face detector",font=("bold",15),fg="white",bg="blue",activebackground="blue",cursor="hand2")
        f_button.place(x=410,y=480,width=250,height=30)

        #3rd button
        third_button=Image.open(r"C:\15\3-2 IP PROJECT\Images\attendance.jpg")
        third_button=third_button.resize((250,350))
        self.p_third_image=ImageTk.PhotoImage(third_button)

        l_third_button=Button(l_bg_img,image=self.p_third_image,cursor="hand2")
        l_third_button.place(x=870,y=130,width=250,height=350)

        f_button=Button(l_bg_img,text="Attendance",command=self.attendance,font=("bold",15),fg="white",bg="blue",activebackground="blue",cursor="hand2")
        f_button.place(x=870,y=480,width=250,height=30)


        #4th button
        fourth_button=Image.open(r"C:\15\3-2 IP PROJECT\Images\training.jpg")
        fourth_button=fourth_button.resize((250,350))
        self.p_fourth_image=ImageTk.PhotoImage(fourth_button)

        l_fourth_button=Button(l_bg_img,image=self.p_fourth_image,cursor="hand2")
        l_fourth_button.place(x=1200,y=130,width=250,height=350)

        f_button=Button(l_bg_img,command=self.train_classifier,text="Train Data",font=("bold",15),fg="white",bg="blue",activebackground="blue",cursor="hand2")
        f_button.place(x=1200,y=480,width=250,height=30)


    #===================train button===============================
    
    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L') 
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            if cv2.waitKey(1) == 13:  # This waits for the Enter key to be pressed
                break
        ids = np.array(ids)

        #=======================classifier=======
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!", parent=self.root)

    
    def stu_detail_button(self):
        self.new_window=Toplevel(self.root)
        self.obj=Student(self.new_window)

    
    def face_detector(self):
        self.new_window=Toplevel(self.root)
        self.obj=Face_detector(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.obj=Attendance(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=facerecognition(root)
    root.mainloop()
