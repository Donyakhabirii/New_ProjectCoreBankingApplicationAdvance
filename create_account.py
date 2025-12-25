from ttkbootstrap import Frame, Label, Entry, Button
from ttkbootstrap.dialogs import Messagebox
from Common.Decorators.performance_logger_decorator import performance_logger

class CreateAccountFrame(Frame):
    def __init__(self, window, view_manager, account_business):
        super().__init__(window)
        self.view_manager = view_manager
        self.account_business = account_business

        Label(self, text="Customer ID:").grid(row=0, column=0, pady=5, padx=5)
        self.customer_entry = Entry(self)
        self.customer_entry.grid(row=0, column=1, pady=5, padx=5)

        Label(self, text="Account Type ID:").grid(row=1, column=0, pady=5, padx=5)
        self.account_type_entry = Entry(self)
        self.account_type_entry.grid(row=1, column=1, pady=5, padx=5)

        Label(self, text="Initial Deposit:").grid(row=2, column=0, pady=5, padx=5)
        self.deposit_entry = Entry(self)
        self.deposit_entry.grid(row=2, column=1, pady=5, padx=5)

        self.create_button = Button(self, text="Create Account", command=self.create_account_clicked)
        self.create_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.back_button = Button(self, text="Back", command=self.back_to_account_management)
        self.back_button.grid(row=4, column=0, columnspan=2, pady=5)

    @performance_logger
    def create_account_clicked(self):
        try:
            customer_id = int(self.customer_entry.get())
            account_type_id = int(self.account_type_entry.get())
            initial_deposit = float(self.deposit_entry.get())

            response = self.account_business.create_account(customer_id, account_type_id, initial_deposit)
            if response.success:
                Messagebox.show_info("Success", f"Account created! ID: {response.data}")
                self.view_manager.show_frame("account_management")
                self.view_manager.frames["account_management"].load_data_to_treeview()
            else:
                Messagebox.show_error("Error", response.message)
        except Exception as e:
            Messagebox.show_error("Error", str(e))

    def back_to_account_management(self):
        self.view_manager.show_frame("account_management")
