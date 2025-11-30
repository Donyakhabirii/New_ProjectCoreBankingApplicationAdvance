#from tkinter import Frame,Label,Entry,Button,messagebox
from ttkbootstrap import Frame,Label,Entry,Button,Treeview
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.style import INFO
#from  tkinter.ttk import Treeview
from Common.Decorators.performance_logger_decorator import performance_logger


class AccountManagementFrame(Frame):
    def __init__(self,window,view_manager,account_business):
        super().__init__(window)
        self.account_business = account_business
        self.view_manager = view_manager

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=1)
        self.grid_rowconfigure(3,weight=1)
        self.header_label = Label(self,text="Account Manager Form")
        self.header_label.grid(row=0,column=0,columnspan=6,padx=10,pady=10)
        self.search_entry=Entry(self)
        self.search_entry.grid(row=1,column=0,pady=(0,10),padx=10,columnspan=5,sticky="ew")
        self.search_button= Button(self,text="Search")
        self.search_button.grid(row=1,column=5,pady=(0,10),padx=(0,10),sticky="w")
        self.create_account_button = Button(self,text="Create Account")
        self.create_account_button.grid(row=2,column=0,pady=(0,10),padx=10,sticky="ew")
        self.update_account_button = Button(self,text="Update Account")
        self.update_account_button.grid(row= 2, column=1,padx=(0,10),pady=(0,10),sticky="ew")
        self.delete_account_button = Button(self,text="Delete Account")
        self.delete_account_button.grid(row=2,column=2,pady=(0,10),padx=(0,10),sticky="ew")
        self.change_status_account_button = Button(self,text="Change Account")
        self.change_status_account_button.grid(row=2,column=3,pady=(0,10),padx=(0,10),sticky="ew")
        self.transaction_button = Button(self,text="Transaction",command=self.transaction_button_clicked,bootstyle=INFO,state="disable")
        self.transaction_button.grid(row=2,column=4,pady=(0,10),padx=(0,10),sticky="ew")
        self.account_list_treeview = Treeview(self,columns=("firstname_owner",
                                                            "lastname_owner",
                                                            "phone_number",
                                                            "account_number",
                                                            "opening_data",
                                                            "account_type",
                                                            "account_status"
                                                            ))
        self.account_list_treeview.heading("#0",text="#")
        self.account_list_treeview.heading("#1",text="First Name")
        self.account_list_treeview.heading("#2", text="Last Name")
        self.account_list_treeview.heading("#3", text="Phone Number")
        self.account_list_treeview.heading("#4", text="Account Number")
        self.account_list_treeview.heading("#5", text="Opening Date")
        self.account_list_treeview.heading("#6", text="Account Type")
        self.account_list_treeview.heading("#7", text="Account Status")
        self.account_list_treeview.column("#0",width=60)
        self.account_list_treeview.grid(row=3,column=0,columnspan=6,padx=10,pady=(0,10),sticky="nsew")

        self.account_list_treeview.bind("<<TreeviewSelect>>",self.treeview_selected)

        self.previous_page_button = Button(self,text="<",command=self.load_previous_data_to_treeview)
        self.previous_page_button.grid(row=4,column=1,pady=(0,10),padx=10,sticky="w")

        self.current_page_label = Label(self,text="1")
        self.current_page_label.grid(row=4,column=2,pady=(0,10),padx=10)

        self.next_page_button = Button(self,text=">",command=self.load_next_data_to_treeview)
        self.next_page_button.grid(row=4,column=3,pady=(0,10),padx=10,sticky="e")

        self.back_to_home_button = Button(self,text="Back to home",command=self.back_to_home_form)
        self.back_to_home_button.grid(row=4,column=0,pady=(0,10),padx=10,sticky="w")
        #pagination section


    @performance_logger
    def back_to_home_form(self):
        self.view_manager.show_frame("home")
    @performance_logger
    def load_data_to_treeview(self,page_number = 1,page_size = 15):
        #Call Business Logic
        response = self.account_business.get_account_list(page_number,page_size)
        if response.success:
            for row in self.account_list_treeview.get_children():
                self.account_list_treeview.delete(row)
            for index,account in enumerate(response.data):
                self.account_list_treeview.insert(
                    "",
                    "end",
                    iid=account.account_id,
                    text=str(index+1),
                    values=(
                        account.customer.first_name,
                        account.customer.last_name,
                        account.customer.phone_number,
                        account.account_number,
                        account.opening_date,
                        account.account_type,
                        account.account_status
                    )
                )
        else:
            Messagebox.show_error(message=response.message,title="Failed!")
    @performance_logger
    def load_next_data_to_treeview(self):
        current_page = int(self.current_page_label.cget("text"))
        next_page = current_page + 1
        self.load_data_to_treeview(next_page)
        self.current_page_label.config(text=str(next_page))
    @performance_logger
    def load_previous_data_to_treeview(self):
        current_page = int(self.current_page_label.cget("text"))
        previous_page = max(current_page - 1, 1)
        self.load_data_to_treeview(previous_page)
        self.current_page_label.config(text=str(previous_page))
    @performance_logger
    def transaction_button_clicked(self):
        transaction_management_frame = self.view_manager.show_frame("transaction_management")
        account_id = int(self.account_list_treeview.selection()[0])
        transaction_management_frame.load_transaction_to_treeview(account_id)

    def treeview_selected(self,event):
        row_selected_count = len(self.account_list_treeview.selection())
        if row_selected_count == 0 or row_selected_count>1:
            self.transaction_button.config(state="disable")
        elif row_selected_count == 1:
            self.transaction_button.config(state="normal")







