#from tkinter import Frame,Label,Entry,Button,messagebox
from ttkbootstrap import Frame,Label,Button,Entry
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap import Combobox
#from tkinter.ttk import Combobox
from Common.Entities.Enums.transaction_types import TransactionTypes
from Common.Decorators.performance_logger_decorator import performance_logger


class CreateTransactionFrame(Frame):
    def __init__(self,window,view_manager,transaction_business):
        super().__init__(window)

        self.grid_columnconfigure(1,weight=1)

        self.view_manger = view_manager
        self.transaction_business = transaction_business

        self.header=Label(self,text="Create Transaction Form")
        self.header.grid(row=0,column=1,pady=10,sticky="w")

        self.amount_label = Label(self,text="Amount")
        self.amount_label.grid(row=1,column=0,pady=(0,10),padx=10,sticky="e")

        self.amount_entry = Entry(self)
        self.amount_entry.grid(row=1,column=1,pady=(0,10),padx=(0,10),sticky="ew")

        self.transaction_type_label = Label(self, text="Type")
        self.transaction_type_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.transaction_type_entry = Combobox(self,values = ("1-Deposit","2-Withdraw"),state = "readonly")
        self.transaction_type_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 10), sticky="ew")

        self.submit_button = Button(self,text="Submit",command=self.create_transaction_button_clicked)
        self.submit_button.grid(row=3, column=1, pady=(0, 10), padx=(0,10), sticky="w")

        self.back_button = Button(self,text="Back to transactions",command=self.back)
        self.back_button.grid(row=4, column=1, pady=(0, 10), padx=(0,10), sticky="w")

        self.account_id = 0
    @performance_logger
    def create_transaction_button_clicked(self):
        amount = float(self.amount_entry.get())
        transaction_type = TransactionTypes(int(self.transaction_type_entry.get().split('-')[0]))

        response = self.transaction_business.create_transaction(amount,transaction_type,self.account_id)
        if response.success:
            frame = self.view_manger.show_frame("transaction_management")
            frame.load_transaction_to_treeview(self.account_id)
        else:
            Messagebox.show_error(title="Transaction Failed!",message=response.message)
    @performance_logger
    def set_account_id(self,account_id:int):
        self.account_id = account_id
    @performance_logger
    def back(self):
        self.view_manger.show_frame("transaction_management")


