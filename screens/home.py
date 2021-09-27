import tkinter as tk
from tkinter import ttk


class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title=tk.Label(self,text="home",font=("times new roman",30,"bold"),bg="white")
        title.place(x=0,y=30,relwidth=1)

        btn_forget=tk.Button(self,text="logout",command=lambda: self.logout(controller),font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E")
        btn_forget.place(x=100,y=390)

    def logout(self,controller):
        controller.str_to_class("Login")