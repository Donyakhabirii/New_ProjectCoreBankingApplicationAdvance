from Presentation.Frames.register import RegisterFrame
from Presentation.Window import ApplicationWindow
from Presentation.Frames.login import Loginframe
from Presentation.Frames.home import HomeFrame
from Presentation.Frames.account_management import AccountManagementFrame
from Presentation.Frames.transaction_management import TransactionManagementFrame
from Presentation.Frames.create_transaction import CreateTransactionFrame
from Presentation.Frames.navbar import NavbarFrame
from BusinessLogic.employee_business_logic import EmployeeBusinessLogic
from BusinessLogic.account_business_logic import AccountBusinessLogic
from Presentation.Frames.profile import ProfileFrame
from BusinessLogic.transaction_business_logic import TransactionBusinessLogic

class ViewManager:
    def __init__(self,
                 employee_business:EmployeeBusinessLogic,
                 account_business : AccountBusinessLogic,
                 transaction_business: TransactionBusinessLogic):
        self.employee_business = employee_business
        self.frames = {}
        self.window = ApplicationWindow()

        self.navbar_frame = NavbarFrame(self.window,self)
        self.navbar_frame.grid(row = 0,column= 0,sticky = "ew")

        self.add_frame("Register",RegisterFrame(self.window,self),(400,250))
        self.add_frame("home", HomeFrame(self.window, self,employee_business),(500,450))
        self.add_frame("account_management",AccountManagementFrame(self.window,self,account_business),(1500,500))
        self.add_frame("transaction_management",TransactionManagementFrame(self.window,self,transaction_business),(700,500))
        self.add_frame("create_transaction", CreateTransactionFrame(self.window, self, transaction_business),(700, 500))
        self.add_frame("login",Loginframe(self.window,self,employee_business),(500,450))
        self.add_frame("profile",ProfileFrame(self.window,self,employee_business),(800,600))
        self.show_frame("login")
        self.resize_window("login")
        self.window.show()
    def add_frame(self,name,frame,size=(400,300)):
        self.frames[name] = (frame,size)
        self.frames[name][0].grid(row = 1, column = 0,sticky = "nsew")

    def show_frame(self,frame_name:str):
        self.resize_window(frame_name)
        frame = self.frames[frame_name][0]
        frame.tkraise()
        return frame
    def resize_window(self,frame_name):
        current_frame_data = self.frames[frame_name]
        frame_size = current_frame_data[1]
        self.window.resize(*frame_size)

    def set_theme(self, theme_name: str):
        self.window.style.theme_use(theme_name)
