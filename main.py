
import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)
from screens.login import Login
from screens.register import Register
from screens.home import Home

import sys




class Application(tk.Tk):
    def __init__(self, *args, **kwargs):        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "software")       
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.von_ueberall_erreichbar = 0
        self.frames = {}
        for F in (Login,Register,Home):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Login)

    def str_to_class(self,classname):
        self.show_frame(getattr(sys.modules[__name__], classname))

    def getVUE(self):
        return self.von_ueberall_erreichbar

    def raiseVUE(self, targetFrame):
        self.von_ueberall_erreichbar += 1           
        self.frames[targetFrame].label2.config(text=self.getVUE())

    def show_frame(self, targetFrame):
        frame = self.frames[targetFrame]
        frame.tkraise()








    


app = Application()
app.attributes('-fullscreen', True)
app.mainloop()
