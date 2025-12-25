from ttkbootstrap import Frame, Label, Entry, Button, Combobox
from ttkbootstrap.dialogs import Messagebox
from Common.Decorators.performance_logger_decorator import performance_logger

class ChangeAccountFrame(Frame):
    def __init__(self, window, view_manager, account_business):
        super().__init__(window)
        self.view_manager = view_manager
        self.account_business = account_business

        self.account_id_label = Label(self, text="Account ID:")
        self.account_id_label.grid(row=0, column=0, pady=5, padx=5)
        self.account_id_entry = Entry(self)
        self.account_id_entry.grid(row=0, column=1, pady=5, padx=5)

        self.account_type_label = Label(self, text="Account Type:")
        self.account_type_label.grid(row=1, column=0, pady=5, padx=5)
        self.account_type_combobox = Combobox(self, values=["Saving", "Current"])
        self.account_type_combobox.grid(row=1, column=1, pady=5, padx=5)

        self.account_status_label = Label(self, text="Account Status:")
        self.account_status_label.grid(row=2, column=0, pady=5, padx=5)
        self.account_status_combobox = Combobox(self, values=["Active", "Blocked"])
        self.account_status_combobox.grid(row=2, column=1, pady=5, padx=5)

        self.save_button = Button(self, text="Save Changes", command=self.save_changes_clicked)
        self.save_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.back_button = Button(self, text="Back", command=self.back_to_account_management)
        self.back_button.grid(row=4, column=0, columnspan=2, pady=5)

    @performance_logger
    def load_account(self, account):
        self.account_id_entry.config(state="normal")
        self.account_id_entry.delete(0, "end")
        self.account_id_entry.insert(0, account.account_id)
        self.account_id_entry.config(state="readonly")

        self.account_type_combobox.set(account.account_type)
        self.account_status_combobox.set("Active" if account.account_status == 1 else "Blocked")

    @performance_logger
    def save_changes_clicked(self):
        try:
            account_id = int(self.account_id_entry.get())
            account_type = self.account_type_combobox.get()
            status_str = self.account_status_combobox.get()
            account_status = 1 if status_str == "Active" else 2
            changes = {}
            if account_type:
                changes["account_type"] = account_type
            changes["account_status"] = account_status
            response = self.account_business.update_account(account_id, changes)
            if response.success:
                Messagebox.show_info("Success", "Account updated successfully :)")
                self.view_manager.show_frame("account_management")
                self.view_manager.frames["account_management"][0].load_data_to_treeview()
            else:
                Messagebox.show_error("Error", response.message)
        except Exception as e:
            Messagebox.show_error("Error", str(e))

    @performance_logger
    def back_to_account_management(self):
        self.view_manager.show_frame("account_management")
