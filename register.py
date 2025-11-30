#from tkinter import Frame, Label, Entry,Button
from ttkbootstrap import Frame,Label,Entry,Button

class RegisterFrame(Frame):
    def __init__(self,window,view_manager):
        super().__init__(window)
        self.view_manager = view_manager
        self.grid_columnconfigure(1,weight=1)
        self.header_label = Label(self,text="Register Form")
        self.header_label.grid(row=0,column=1,pady=10,sticky="w")
        self.username_label = Label(self,text="Username")
        self.username_label.grid(row=1,column=0,pady=(0,10),padx=10,sticky="e")
        self.username_entry = Entry(self)
        self.username_entry.grid(row=1,column=1,pady=(0,10),padx=(0,10),sticky="ew")
        self.password_label = Label(self,text="Password")
        self.password_label.grid(row=2,column=0,pady=(0,10),padx=10,sticky="e")
        self.password_entry = Entry(self)
        self.password_entry.grid(row=2,column=1,pady=(0,10),padx=(0,10),sticky="ew")
        self.register_button = Button(self,text="Register")
        self.register_button.grid(row=5,column=1,pady=(0,10),padx=(0,10),sticky="w")
        self.back_to_login_button = Button(self,text="Back to Login",command=lambda: self.view_manager.show_frame("login"))
        self.back_to_login_button.grid(row=6, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

