from ttkbootstrap import Frame, Label, Entry, Button
from ttkbootstrap.dialogs import Messagebox
from Common.Decorators.performance_logger_decorator import performance_logger

class UpdateAccountFrame(Frame):
    def __init__(self, window, view_manager, account_business):
        super().__init__(window)
        self.view_manager = view_manager
        self.account_business = account_business

        Label(self, text="Account Number:").grid(row=0, column=0, pady=5, padx=5)
        self.account_number_entry = Entry(self)
        self.account_number_entry.grid(row=0, column=1, pady=5, padx=5)

        Label(self, text="Account Type:").grid(row=1, column=0, pady=5, padx=5)
        self.account_type_entry = Entry(self)
        self.account_type_entry.grid(row=1, column=1, pady=5, padx=5)

        Label(self, text="Account Status:").grid(row=2, column=0, pady=5, padx=5)
        self.account_status_entry = Entry(self)
        self.account_status_entry.grid(row=2, column=1, pady=5, padx=5)

        self.save_button = Button(self, text="Save Changes", command=self.save_changes)
        self.save_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.back_button = Button(self, text="Back", command=self.back_to_account_management)
        self.back_button.grid(row=4, column=0, columnspan=2, pady=5)
        self.current_account_id = None
    @performance_logger
    def load_account(self, account_id: int):
        account = self.account_business.account_repository.get_account_by_id(account_id)
        if not account:
            Messagebox.show_error("Error", "Account not found")
            return
        self.current_account_id = account.account_id
        self.account_number_entry.delete(0, "end")
        self.account_number_entry.insert(0, account.account_number)
        self.account_type_entry.delete(0, "end")
        self.account_type_entry.insert(0, account.account_type)
        self.account_status_entry.delete(0, "end")
        self.account_status_entry.insert(0, account.account_status)
    @performance_logger
    def save_changes(self):
        if self.current_account_id is None:
            Messagebox.show_error("Error", "No account loaded")
            return
        account_number = self.account_number_entry.get()
        account_type = self.account_type_entry.get()
        account_status = self.account_status_entry.get()
        changes = {
            "account_number": account_number,
            "account_type_id": account_type,
            "account_status_id": account_status
        }
        response = self.account_business.update_account(self.current_account_id, changes)
        if response.success:
            Messagebox.show_info("Success", "Account updated successfully")
            self.view_manager.show_frame("account_management")
            self.view_manager.frames["account_management"][0].load_data_to_treeview()
        else:
            Messagebox.show_error("Error", response.message)
    @performance_logger
    def back_to_account_management(self):
        self.view_manager.show_frame("account_management")
