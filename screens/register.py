
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import bcrypt

from .database import *

class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        login_frame=tk.Frame(self,bd=2,relief=tk.RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=520)
        title=tk.Label(login_frame,text="register system",font=("times new roman",30,"bold"),bg="white")
        title.place(x=0,y=30,relwidth=1)
        
        username=tk.Label(login_frame,text="username",font=("times new roman",15),bg="white",fg="#767171")
        username.place(x=50,y=100)
        self.username=tk.StringVar() 
        self.usernameentry=tk.Entry(login_frame,textvariable=self.username,font=("times new roman",15),bg="#ECECEC")
        self.usernameentry.place(x=50,y=140,width=250)
        
        password=tk.Label(login_frame,text="Password",font=("times new roman",15),bg="white",fg="#767171")
        password.place(x=50,y=200)
        self.password=tk.StringVar()
        self.passwordentry=tk.Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC")
        self.passwordentry.place(x=50,y=240,width=250)

        confirmpassword=tk.Label(login_frame,text="confirm Password",font=("times new roman",15),bg="white",fg="#767171")
        confirmpassword.place(x=50,y=300)
        self.confirmpassword=tk.StringVar()
        self.confirmpasswordentry=tk.Entry(login_frame,textvariable=self.confirmpassword,show="*",font=("times new roman",15),bg="#ECECEC")
        self.confirmpasswordentry.place(x=50,y=340,width=250)
        
        btn_login=tk.Button(login_frame,text="register",command=self.registeruser,font=("times new roman",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2")
        btn_login.place(x=50,y=400,width=250,height=35)

        login=tk.Button(login_frame,text="login",command=lambda: self.loginpage(controller),font=("times new roman",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2")
        login.place(x=50,y=450,width=250,height=35)


    def loginpage(self,controller):
        controller.str_to_class("Login")

    def registeruser(self):
        username=self.username.get()
        password=self.password.get()
        confirmpassword=self.confirmpassword.get()
        self.usernameentry.delete(0, 'end')
        self.passwordentry.delete(0, 'end')
        self.confirmpasswordentry.delete(0, 'end')
        if username!="" and password!="" and confirmpassword!="":
            if password==confirmpassword:
                password = bytes(password, 'utf-8')
                password = bcrypt.hashpw(password, bcrypt.gensalt(14))
                userexists = mycol.count_documents({"username" : username})
                if userexists>0:
                    messagebox.askretrycancel("error", " user exists Try again?") 
                else:
                    mydict = {"_id":mycol.find().count()+1,"username":username,"password":password}
                    x = mycol.insert_one(mydict)
            else:
                messagebox.askretrycancel("error", " password dosent match") 
        else:
            messagebox.askretrycancel("error", "please enter all fields") 











        
        