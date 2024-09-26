from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import os
import csv

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1526x795+0+0")
        self.root.title("Student Details")

        # Variables
        self.var_attend_id = StringVar()
        self.var_attend_roll = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_attendance = StringVar()

        # Image 1
        img1 = Image.open(r"C:\15\3-2 IP PROJECT\Images\img1.png")
        img1 = img1.resize((800, 200))
        self.p_img1 = ImageTk.PhotoImage(img1)
        l_img1 = Label(self.root, image=self.p_img1)
        l_img1.place(x=0, y=0, width=800, height=200)

        # Image 2
        img2 = Image.open(r"C:\15\3-2 IP PROJECT\Images\img2.jpg")
        img2 = img2.resize((800, 200))
        self.p_img2 = ImageTk.PhotoImage(img2)
        l_img2 = Label(self.root, image=self.p_img2)
        l_img2.place(x=800, y=0, width=800, height=200)

        # Background
        bg_img = Image.open(r"C:\15\3-2 IP PROJECT\Images\home_bg.webp")
        bg_img = bg_img.resize((1526, 675))
        self.p_bg_img = ImageTk.PhotoImage(bg_img)
        l_bg_img = Label(self.root, image=self.p_bg_img)
        l_bg_img.place(x=0, y=200, width=1526, height=675)

        # Title
        l_title = Label(l_bg_img, text="Attendance", font=("bold", 35), bg="black", fg="white")
        l_title.place(x=0, y=0, width=1526, height=50)

        # Main frame
        main_frame = Frame(l_bg_img, bd=2, background="white")
        main_frame.place(x=18, y=55, width=1490, height=625)

        # Left frame
        left_frame = LabelFrame(main_frame, bd=6, relief=RIDGE, text="Student Attendance Details", font=("bold", 10, "bold"), foreground="black", background="#3AAFA9")
        left_frame.place(x=10, y=10, width=730, height=600)

        l_img = Image.open(r"C:\15\3-2 IP PROJECT\Images\SD_left_frame.jpg")
        l_img = l_img.resize((718, 110))
        self.p_lfi = ImageTk.PhotoImage(l_img)
        lf_l_img = Label(left_frame, image=self.p_lfi)
        lf_l_img.place(x=0, y=0, width=718, height=110)

        Left_inside_frame = LabelFrame(left_frame, bd=2, relief=RIDGE)
        Left_inside_frame.place(x=5, y=115, width=710, height=300)

        # Student ID
        stuId_label = Label(Left_inside_frame, text="Student Id:", font=("thin", 12))
        stuId_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        stuId_entry = ttk.Entry(Left_inside_frame, textvariable=self.var_attend_id, width=30, foreground="grey")
        stuId_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Roll Number
        roll_label = Label(Left_inside_frame, text="Student Roll:", font=("thin", 12))
        roll_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)
        roll_entry = ttk.Entry(Left_inside_frame, width=30, textvariable=self.var_attend_roll, foreground="grey")
        roll_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # Student Name
        stuName_label = Label(Left_inside_frame, text="Name:", font=("thin", 12))
        stuName_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        stuName_entry = ttk.Entry(Left_inside_frame, textvariable=self.var_attend_name, width=30, foreground="grey")
        stuName_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Department
        stuDep_label = Label(Left_inside_frame, text="Department:", font=("thin", 12))
        stuDep_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        stuDep_entry = ttk.Entry(Left_inside_frame, textvariable=self.var_attend_dep, width=30, foreground="grey")
        stuDep_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # Time
        stuTime_label = Label(Left_inside_frame, text="Time:", font=("thin", 12))
        stuTime_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        stuTime_entry = ttk.Entry(Left_inside_frame, textvariable=self.var_attend_time, width=30, foreground="grey")
        stuTime_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # Date
        stuDate_label = Label(Left_inside_frame, text="Date:", font=("thin", 12))
        stuDate_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        stuDate_entry = ttk.Entry(Left_inside_frame, textvariable=self.var_attend_date, width=30, foreground="grey")
        stuDate_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        # Attendance Status
        status_label = Label(Left_inside_frame, text="Course", font=("thin", 12))
        status_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        status_combo = ttk.Combobox(Left_inside_frame, textvariable=self.var_attend_attendance, font=("thin", 12), width=22, state="readonly")
        status_combo["values"] = ["Status", "Present", "Absent"]
        status_combo.current(0)
        status_combo.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Button frame
        but_frame = Frame(Left_inside_frame, bd=2, relief=RIDGE)
        but_frame.place(x=0, y=200, width=697, height=60)
        Import_but = Button(but_frame, command=self.importCsv, text="Import", font=("thin", 10), width=43, cursor="hand2")
        Import_but.grid(row=0, column=0)
        Export_but = Button(but_frame, command=self.exportCsv, text="Export csv", font=("thin", 10), width=41, cursor="hand2")
        Export_but.grid(row=0, column=1)
        update_but = Button(but_frame, text="Update", command=self.updateCsv, font=("thin", 10), width=43, cursor="hand2")
        update_but.grid(row=1, column=0)
        reset_but = Button(but_frame, text="Reset", command=self.reset_data, font=("thin", 10), width=41, cursor="hand2")
        reset_but.grid(row=1, column=1)

        # Right frame
        right_frame = LabelFrame(main_frame, bd=6, relief=RIDGE, text="Attendance Details", font=("bold", 10, "bold"), foreground="black", background="light blue")
        right_frame.place(x=750, y=10, width=730, height=600)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=5, width=705, height=490)

        # Scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.AttendanceTable = ttk.Treeview(table_frame, column=("id", "roll", "Name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceTable.xview)
        scroll_y.config(command=self.AttendanceTable.yview)
        self.AttendanceTable.heading("id", text="Attendance ID")
        self.AttendanceTable.heading("roll", text="Roll")
        self.AttendanceTable.heading("Name", text="Name")
        self.AttendanceTable.heading("department", text="Department")
        self.AttendanceTable.heading("time", text="Time")
        self.AttendanceTable.heading("date", text="Date")
        self.AttendanceTable.heading("attendance", text="Attendance")
        self.AttendanceTable["show"] = "headings"
        self.AttendanceTable.column("id", width=100)
        self.AttendanceTable.column("roll", width=100)
        self.AttendanceTable.column("Name", width=100)
        self.AttendanceTable.column("department", width=100)
        self.AttendanceTable.column("time", width=100)
        self.AttendanceTable.column("date", width=100)
        self.AttendanceTable.column("attendance", width=100)
        self.AttendanceTable.pack(fill=BOTH, expand=1)
        self.AttendanceTable.bind("<ButtonRelease>", self.get_cursor)

    def fetchData(self, rows):
        self.AttendanceTable.delete(*self.AttendanceTable.get_children())
        for i in rows:
            self.AttendanceTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()  # Clear the list before importing new data
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
            parent=self.root
        )
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data Found to Export", "No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
                parent=self.root,
                defaultextension=".csv"
            )
            if not fln:
                return
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", f"Your data exported to {os.path.basename(fln)} successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceTable.focus()
        content = self.AttendanceTable.item(cursor_row)
        rows = content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")

    def updateCsv(self):
        try:
            global mydata
            if len(mydata) < 1:
                messagebox.showerror("No Data Found to Update", "No data found to update", parent=self.root)
                return False

            stu_id = self.var_attend_id.get()
            updated = False
            for i, row in enumerate(mydata):
                if len(row) > 0 and row[0] == stu_id:
                    mydata[i] = [
                        self.var_attend_id.get(),
                        self.var_attend_roll.get(),
                        self.var_attend_name.get(),
                        self.var_attend_dep.get(),
                        self.var_attend_time.get(),
                        self.var_attend_date.get(),
                        self.var_attend_attendance.get()
                    ]
                    updated = True
                    break

            if not updated:
                messagebox.showerror("Error", "Student ID not found", parent=self.root)
                return False

            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
                parent=self.root,
                defaultextension=".csv"
            )
            if not fln:
                return

            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Updated", f"Your data updated and saved to {os.path.basename(fln)} successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
