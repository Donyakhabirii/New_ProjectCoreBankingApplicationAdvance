#from tkinter import Frame, Label, Button, messagebox, filedialog
#from tkinter.ttk import Treeview
from ttkbootstrap import Frame,Label,Button,Treeview
from ttkbootstrap.dialogs import Messagebox
from tkinter import filedialog
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet


class TransactionManagementFrame(Frame):
    def __init__(self, window, view_manager, transaction_business):
        super().__init__(window)

        self.view_manager = view_manager
        self.transaction_business = transaction_business

        # Pagination tracking
        self.current_account_id = None
        self.current_page = 1
        self.page_size = 15

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.header_label = Label(self, text="Transaction Manager Form")
        self.header_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        self.account_info_label = Label(self)
        self.account_info_label.grid(row=1, column=0, columnspan=2, pady=(0, 10), padx=10)

        self.create_transaction_button = Button(self, text="Create Transaction",command=self.create_transaction_button_clicked)
        self.create_transaction_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="ew")

        self.export_pdf_transaction_button = Button(
            self, text="Export to PDF", command=self.export_pdf_transaction_button_clicked
        )
        self.export_pdf_transaction_button.grid(row=2, column=1, pady=(0, 10), padx=10, sticky="ew")

        self.transaction_treeview = Treeview(
            self, columns=("amount", "transaction_type", "transaction_time")
        )
        self.transaction_treeview.column("#0", width=60)
        self.transaction_treeview.heading("#0", text="#")
        self.transaction_treeview.heading("amount", text="Amount")
        self.transaction_treeview.heading("transaction_type", text="Transaction Type")
        self.transaction_treeview.heading("transaction_time", text="Transaction Time")
        self.transaction_treeview.grid(row=3, column=0, columnspan=2, pady=(0, 10), padx=10, sticky="nsew")

        self.account_id = 0

        # Pagination buttons
        self.previous_page_button = Button(self, text="<", command=self.load_previous_data_to_treeview)
        self.previous_page_button.grid(row=4, column=0, pady=(0, 10), padx=10, sticky="w")

        self.current_page_label = Label(self, text="1")
        self.current_page_label.grid(row=4, column=0, pady=(0, 10), padx=10)

        self.next_page_button = Button(self, text=">", command=self.load_next_data_to_treeview)
        self.next_page_button.grid(row=4, column=1, pady=(0, 10), padx=10, sticky="e")

    def load_transaction_to_treeview(self, account_id: int, page_number=1, page_size=15):
        self.account_id = account_id
        self.current_account_id = account_id
        self.current_page = page_number
        self.page_size = page_size

        response = self.transaction_business.get_transaction_list(account_id, page_number, page_size)

        if response.success:
            for row in self.transaction_treeview.get_children():
                self.transaction_treeview.delete(row)

            for index, transaction in enumerate(response.data):
                self.transaction_treeview.insert(
                    "",
                    "end",
                    iid=transaction.transaction_id,
                    text=str(index + 1),
                    values=(transaction.amount, transaction.transaction_type.name, transaction.transaction_time)
                )
            # Update page label
            self.current_page_label.config(text=str(self.current_page))
        else:
            Messagebox.show_error(message=response.message, title="Transaction Failed!")

    def load_next_data_to_treeview(self):
        if self.current_account_id is None:
            return
        self.load_transaction_to_treeview(self.current_account_id, self.current_page + 1, self.page_size)

    def load_previous_data_to_treeview(self):
        if self.current_account_id is None:
            return
        prev_page = max(self.current_page - 1, 1)
        self.load_transaction_to_treeview(self.current_account_id, prev_page, self.page_size)

    def export_pdf_transaction_button_clicked(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Save as Transaction Report"
        )
        if not file_path:
            return
        logo_path = filedialog.askopenfilename(
            title="Select Logo Image (required)",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"), ("All files", "*.*")]
        )

        if not logo_path:
            Messagebox.show_error("Logo required", "You must select a logo image.")
            return

        response = self.transaction_business.export_to_pdf(self.account_id, file_path, logo_path)
        if not response.success:
            Messagebox.show_error(title="Export Failed!", message=response.message)

    def create_transaction_button_clicked(self):
        frame = self.view_manager.show_frame("create_transaction")
        frame.set_account_id(self.account_id)








