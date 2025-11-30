#from tkinter import Frame, Label, Entry, Button, StringVar
from ttkbootstrap import Frame,Label,Entry,Button
from ttkbootstrap.style import INFO
from tkinter import StringVar
import random
import string


class CaptchaComponent(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.captcha_text = StringVar()

        self.generate_new_captcha()
        self.captcha_label = Label(self, textvariable=self.captcha_text,font=("Calibri", 14, "bold"),width=8, bootstyle=INFO)
        self.captcha_label.grid(row=0, column=0, padx=(0, 10))

        self.captcha_entry = Entry(self,width=10)
        self.captcha_entry.grid(row=0, column=1, sticky="ew")

        self.refresh_button = Button(self, text="refresh", command=self.generate_new_captcha,bootstyle=INFO)
        self.refresh_button.grid(row=0, column=2, padx=(10, 0))

    def generate_new_captcha(self):
        letters = f"{string.ascii_uppercase}{string.digits}"
        captcha_chars = []
        for _ in range(5):
            captcha_chars.append(random.choice(letters))
        captcha = ''.join(captcha_chars)
        self.captcha_text.set(captcha)

    def get_captcha_value(self):
        return self.captcha_entry.get()

    def get_captcha_text(self):
        return self.captcha_text.get()

    def is_valid(self):
        return self.get_captcha_value().strip().upper() == self.get_captcha_text().strip().upper()