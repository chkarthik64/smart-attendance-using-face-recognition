from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1450x800+0+0")

        img=Image.open("C:\\15\\3-2 IP PROJECT\\Images\\home_bg.jpeg")
        img = img.resize((1450, 800)) 
        self.bg = ImageTk.PhotoImage(img)



        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open("C:\\15\\3-2 IP PROJECT\\Images\\end-user.png")
        img1=img1.resize((100,100))
        self.photoimage1=ImageTk.PhotoImage(img1)
        limg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        limg1.place(x=730,y=175,width=100,height=100)

        uname=lbl=Label(frame,text="username",font=("times new roman",15,"bold"),fg="white",bg="black")
        uname.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        psw=lbl=Label(frame,text="password",font=("times new roman",15,"bold"),fg="white",bg="black")
        psw.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        login_button=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,
                            fg="white",bg="red",activeforeground="white",activebackground="red")
        login_button.place(x=110,y=300,width=120,height=35)

        register_button=Button(frame,text="New Register",font=("times new roman",15,"bold"),borderwidth=0,
                            fg="white",bg="black",activeforeground="white",activebackground="black")
        register_button.place(x=20,y=350,width=160)

        login_button=Button(frame,text="Forget Password",font=("times new roman",15,"bold"),borderwidth=0,
                            fg="white",bg="black",activeforeground="white",activebackground="black")
        login_button.place(x=20,y=390,width=160)




if __name__=="__main__":
    root=Tk()
    app=login_window(root)
    root.mainloop()