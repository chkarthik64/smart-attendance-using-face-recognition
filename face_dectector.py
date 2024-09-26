from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from Student import Student
import os
import mysql.connector
import numpy as np
import cv2
from time import strftime
from datetime import datetime

class Face_detector:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1526x795+0+0")
        self.root.title("face detector")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Times new roman", 35, "bold"), background="white", foreground="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ==============left image====================
        left_img = Image.open(r"C:\15\3-2 IP PROJECT\Images\home_bg.jpeg")
        left_img = left_img.resize((650, 750))
        self.p_left_img = ImageTk.PhotoImage(left_img)

        l_left_img = Label(self.root, image=self.p_left_img)
        l_left_img.place(x=0, y=45, width=650, height=749)

        # =========================right image=============
        right_img = Image.open(r"C:\15\3-2 IP PROJECT\Images\SD_left_frame.jpg")
        right_img = right_img.resize((950, 750))
        self.p_right_img = ImageTk.PhotoImage(right_img)

        l_right_img = Label(self.root, image=self.p_right_img)
        l_right_img.place(x=650, y=45, width=950, height=749)

        # ===========================button=============
        btn = Button(l_right_img, command=self.face_recog, text="Detect", width=15, font=("bold", 15), bg="blue", fg="black", cursor="hand2")
        btn.place(x=400, y=600, width=250, height=40)


        #===========================attendance=================
    def mark_attendance(self, i, r, n, d):
        with open("attendance6.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.strip().split(",")
                name_list.append(entry[:4])     

            # Create a unique entry for the current record
            current_entry = [str(i), str(r), str(n), str(d)]
            
            
            if current_entry not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")




    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coor = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="kaaki#rootsql64",
                        database="studentregistration"
                    )
                    my_cur = conn.cursor()

                    my_cur.execute("SELECT name FROM student WHERE student_id=%s", (id,))
                    n = my_cur.fetchone()
                    n = n[0] if n else "Unknown"

                    my_cur.execute("SELECT roll_no FROM student WHERE student_id=%s", (id,))
                    r = my_cur.fetchone()
                    r = r[0] if r else "Unknown"

                    my_cur.execute("SELECT dep FROM student WHERE student_id=%s", (id,))
                    d = my_cur.fetchone()
                    d = d[0] if d else "Unknown"

                    my_cur.execute("SELECT student_id FROM student WHERE student_id=%s", (id,))
                    i = my_cur.fetchone()
                    i = i[0] if i else "Unknown"

                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                    continue
                finally:
                    if conn.is_connected():
                        my_cur.close()
                        conn.close()

                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coor = [x, y, w, h]

            return coor


        def recognize(img, clf, faceCascade):
            coor = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_detector(root)
    root.mainloop()