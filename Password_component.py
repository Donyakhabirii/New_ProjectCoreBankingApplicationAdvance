#from tkinter import Frame,Entry,Button
from ttkbootstrap import Frame,Entry,Button
from ttkbootstrap.style import INFO
class PasswordComponent(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.current_status = "Hide"
        self.grid_columnconfigure(0,weight=1)
        self.passord_entry = Entry(self,show="*")
        self.passord_entry.grid(row =0,column=0,sticky="ew")
        self.password_status_button = Button(self,text="show",command=self.change_status,bootstyle=INFO)
        self.password_status_button.grid(row =0,column=1,sticky="w")
    def change_status(self):
        if self.current_status == "Hide":
            self.current_status = "show"
            self.password_status_button.config(text="Hide")
            self.passord_entry.config(show="")
        else:
            self.current_status = "Hide"
            self.password_status_button.config(text="show")
            self.passord_entry.config(show="*")

    def get_password_value(self):
        passord_value = self.passord_entry.get()
        return passord_value
    def clear(self):
        self.passord_entry.delete(0,"end")