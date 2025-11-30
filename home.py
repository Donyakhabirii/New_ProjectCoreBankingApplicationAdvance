#from tkinter import Frame,Label,Button
from ttkbootstrap import Frame,Label,Button
from ttkbootstrap.style import INFO
from ttkbootstrap.dialogs import Messagebox
from Common.Entities.employee import Employee
from Common.Decorators.performance_logger_decorator import performance_logger



class HomeFrame(Frame):
    def __init__(self,window,view_manager,employee_business):
        super().__init__(window)

        self.view_manager = view_manager
        self.employee_business = employee_business

        self.grid_columnconfigure(0,weight=1)
        self.header_label = Label(self)
        self.header_label.grid(row=0,column=0,pady=10,padx=10)
        self.profile_management_button = Button(self,text="My Profile",command= self.show_profile)
        self.profile_management_button.grid(row=1,column=0,pady=(0,10),padx=10,sticky="ew")
        self.account_management_button = Button(self,text="Account_management",command= self.show_account_management_form)
        self.account_management_button.grid(row=2,column=0,pady=(0,10),padx=10,sticky="ew")
        self.logout_button = Button(self,text="Logout",command=self.logout,bootstyle=INFO)
        self.logout_button.grid(row=3,column=0,pady=(0,10),padx=10,sticky="ew")

    @performance_logger
    def set_current_user(self,current_user = None):
        if current_user is None:
            current_user = self.employee_business.current_user
        if current_user:
            self.header_label.config(text=f"Welcome {current_user.get_full_name()}")
    @performance_logger
    def logout(self):
        self.view_manager.show_frame("login")
    @performance_logger
    def show_account_management_form(self):
        account_management_frame = self.view_manager.show_frame("account_management")
        account_management_frame.load_data_to_treeview()
    @performance_logger
    def show_profile(self):
        current_user = self.employee_business.current_user
        if not current_user:
            Messagebox.show_error("Error","No user is logged in:)")
            return
        profile_frame = self.view_manager.show_frame("profile")
        profile_frame.load_employee(current_user.ID)

