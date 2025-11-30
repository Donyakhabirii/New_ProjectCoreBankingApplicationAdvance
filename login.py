#from tkinter import Frame, Label,Entry,Button,Checkbutton,messagebox
from ttkbootstrap import Frame,Label,Button,Checkbutton,Entry
from ttkbootstrap.style import SUCCESS
from ttkbootstrap.dialogs import Messagebox
from Presentation.Components.Password_component import PasswordComponent
from Presentation.Components.Captcha_component import CaptchaComponent
from BusinessLogic.employee_business_logic import EmployeeBusinessLogic
from Common.Decorators.performance_logger_decorator import performance_logger



class Loginframe(Frame):
    def __init__(self,window,view_manager,employee_business:EmployeeBusinessLogic):
        super().__init__(window)
        self.view_manager = view_manager
        self.employee_business = employee_business
        self.view_manager = view_manager
        self.grid_columnconfigure(1,weight=1)
        self.header_label = Label(self,text="Login Form")
        self.header_label.grid(row=0,column=1,pady=10,sticky="w")
        self.username_label = Label(self,text="Username")
        self.username_label.grid(row=1,column=0,pady=(0,10),padx=10,sticky="e")
        self.username_entry = Entry(self)
        self.username_entry.grid(row=1,column=1,pady=(0,10),padx=(0,10),sticky="ew")
        self.password_label = Label(self,text="Password")
        self.password_label.grid(row=2,column=0,pady=(0,10),padx=10,sticky="e")
        self.Password_component = PasswordComponent(self)
        self.Password_component.grid(row=2,column=1,pady=(0,10),padx=(0,10),sticky="ew")
        self.captcha_component = CaptchaComponent(self)
        self.captcha_component.grid(row=3, column=1, pady=(0, 10), padx=(0, 10), sticky="ew")
        self.remember_me_Checkbutton = Checkbutton(self,text="Remember me",bootstyle="round-toggle")
        self.remember_me_Checkbutton.grid(row=4,column=1,pady=(0,10),padx=(0,10),sticky="w")
        self.login_button = Button(self,text="Login",command=self.login_button_clicked)
        self.login_button.grid(row=5,column=1,pady=(0,10),padx=(0,10),sticky="w")
        self.register_button = Button(self,text="Register",command=self.go_to_register,bootstyle=SUCCESS)
        self.register_button.grid(row=6,column=1,pady=(0,10),padx=(0,10),sticky="w")
    @performance_logger
    def login_button_clicked(self):
        username = self.username_entry.get()
        password = self.Password_component.get_password_value()

        response = self.employee_business.login(username,password)
        if response.success:
            home_frame = self.view_manager.show_frame("home")
            home_frame.set_current_user(self.employee_business.current_user)
            self.username_entry.delete(0,"end")
            self.Password_component.clear()
        else:
            Messagebox.show_error(title="failed",message=response.message)

    def go_to_register(self):
        self.view_manager.show_frame("Register")