
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox,ttk
from tkinter import messagebox
from .database import *

import bcrypt

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        phone_image=ImageTk.PhotoImage(file="images/phone2.png")
        login_frame=tk.Frame(self,bd=2,relief=tk.RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)
        title=tk.Label(login_frame,text="Login System",font=("times new roman",30,"bold"),bg="white")
        title.place(x=0,y=30,relwidth=1)
        
        name=tk.Label(login_frame,text="User Name",font=("times new roman",15),bg="white",fg="#767171")
        name.place(x=50,y=100)
        self.username=tk.StringVar()
        
        self.usernameentry=tk.Entry(login_frame,textvariable=self.username,font=("times new roman",15),bg="#ECECEC")
        self.usernameentry.place(x=50,y=140,width=250)
        
        lbl_pass=tk.Label(login_frame,text="Password",font=("times new roman",15),bg="white",fg="#767171")
        lbl_pass.place(x=50,y=200)
        self.password=tk.StringVar()
        
        self.passwordentry=tk.Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC")
        self.passwordentry.place(x=50,y=240,width=250)
        
        btn_login=tk.Button(login_frame,text="Log In",command=lambda: self.checklogin(controller),font=("times new roman",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2")
        btn_login.place(x=50,y=300,width=250,height=35)
        
        hr=tk.Label(login_frame,bg="lightgray")
        hr.place(x=50,y=370,width=250,height=2)
        
        or_=tk.Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold"))
        or_.place(x=150,y=355)
        
        btn_forget=tk.Button(login_frame,text="Forget Password?",font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E")
        btn_forget.place(x=100,y=390)
        
        #---------Sign Up? tk.Frame-----------#
        register_frame=tk.Frame(self,bd=2,relief=tk.RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)
        
        lbl_reg=tk.Label(register_frame,text="Don't have an account?",font=("times new roman",13),bg="white")
        lbl_reg.place(x=40,y=20)
        
        btn_signup=tk.Button(register_frame,text="Sign Up",command=lambda: self.registerpage(controller),font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E")
        btn_signup.place(x=215,y=16)
        
        #-------Animation Images------------#
        self.im1=ImageTk.PhotoImage(file="images/animi1.png")
        self.im2=ImageTk.PhotoImage(file="images/animi2.png")
        self.im3=ImageTk.PhotoImage(file="images/animi3.png")
        
        self.lbl_change_image=tk.Label(self,bg="white")
        self.lbl_change_image.place(x=328,y=169,width=240,height=428)
        
        self.animate()

        
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
        
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,tk.END)
        self.txt_answer.delete(0,tk.END)
        self.email.set('')
        self.password.set('')

    
    def registerpage(self,controller):
        controller.str_to_class("Register")

    def checklogin(self,controller):
        username=self.username.get()
        password=self.password.get()
        self.usernameentry.delete(0, 'end')
        self.passwordentry.delete(0, 'end')
        password = bytes(password, 'utf-8')
        user= mycol.find({"username" : username})
        userexists = mycol.count_documents({"username" : username})
        if username!="" and password!="":
            if userexists>0:
                for i in user:
                    hashed=i['password']
                    if bcrypt.checkpw(password, hashed):
                        controller.str_to_class("Home")
                    else:
                        messagebox.askretrycancel("error", " incorrect username or password")
            else:
                messagebox.askretrycancel("error", " user dosenot exists")


        else:
            messagebox.askretrycancel("error", " please enter all details")
        
 



        
