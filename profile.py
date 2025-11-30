#from tkinter import Frame, Label, Button, Entry,messagebox,filedialog
from ttkbootstrap import Frame,Label,Button,Entry
from ttkbootstrap.dialogs import Messagebox
from tkinter import filedialog
import os,time
from PIL import Image,ImageTk
from Common.Entities.employee import Employee



class ProfileFrame(Frame):
    def __init__(self, window, view_manager,employee_business):
        super().__init__(window)
        self.view_manager = view_manager
        self.employee_business = employee_business


        self.grid_columnconfigure(1, weight=1)

        self.header_label = Label(self,text="Show All Information")
        self.header_label.grid(row=0,column=0,pady=10,padx=10,sticky="w")

        self.firstname_label = Label(self,text="First Name")
        self.firstname_label.grid(row=1,column=0,pady=(0,10),padx=10,sticky="e")
        self.firstname_entry = Entry(self)
        self.firstname_entry.grid(row=1,column=1,pady=(0,10),padx=10,sticky="ew")

        self.lastname_label = Label(self,text="Last Name")
        self.lastname_label.grid(row=2,column=0,pady=(0,10),padx=10,sticky="e")
        self.lastname_entry = Entry(self)
        self.lastname_entry.grid(row=2,column=1,pady=(0,10),padx=10,sticky="ew")

        self.Nationalcode_label = Label(self, text="National Code")
        self.Nationalcode_label.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="e")
        self.Nationalcode_entry = Entry(self)
        self.Nationalcode_entry.grid(row=3, column=1, pady=(0, 10), padx=10, sticky="ew")

        self.email_label = Label(self, text="Email")
        self.email_label.grid(row=4, column=0, pady=(0, 10), padx=10, sticky="e")
        self.email_entry = Entry(self)
        self.email_entry.grid(row=4, column=1, pady=(0, 10), padx=10, sticky="ew")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=5, column=0, pady=(0, 10), padx=10, sticky="e")
        self.username_entry = Entry(self)
        self.username_entry.grid(row=5, column=1, pady=(0, 10), padx=10, sticky="ew")

        self.employeestatus_label = Label(self, text="EmployeeStatusID")
        self.employeestatus_label.grid(row=6, column=0, pady=(0, 10), padx=10, sticky="e")
        self.employeestatus_entry = Entry(self)
        self.employeestatus_entry.grid(row=6, column=1, pady=(0, 10), padx=10, sticky="ew")

        self.roleid_label = Label(self, text="RoleId")
        self.roleid_label.grid(row=7, column=0, pady=(0, 10), padx=10, sticky="e")
        self.roleid_entry = Entry(self)
        self.roleid_entry.grid(row=7, column=1, pady=(0, 10), padx=10, sticky="ew")

        self.back_button = Button(self, text="Back to Home", command=self.back_to_home)
        self.back_button.grid(row=8, column=0, pady=(0, 10), padx=10, sticky="w")

        self.Reset_header_label = Label(self,text="Reset Password")
        self.Reset_header_label.grid(row=9,column=0,pady=(0,10),padx=10,sticky="w")
        self.new_password_label = Label(self,text="New Password")
        self.new_password_label.grid(row=10,column=0,pady=(0,10),padx=10,sticky="e")
        self.new_password_entry = Entry(self)
        self.new_password_entry.grid(row=10,column=1,pady=(0,10),padx=10,sticky="ew")
        self.confirm_password_label = Label(self,text="Confirm New Password")
        self.confirm_password_label.grid(row=11,column=0,pady=(0,10),padx=10,sticky="e")
        self.confirm_password_entry = Entry(self)
        self.confirm_password_entry.grid(row=11,column=1,pady=(0,10),padx=10,sticky="ew")
        self.reset_password_button = Button(self,text="Reset Password",command=self.reset_password)
        self.reset_password_button.grid(row=12,column=0,pady=(0,10),padx=10,sticky="e")

        self.upload_header_label = Label(self, text="Upload Image")
        self.upload_header_label.grid(row=13, column=0, pady=(0,10), padx=10, sticky="w")
        self.image_preview_label = Label(self, text="No image",  padding=(20, 80), bootstyle="info", anchor="center")
        self.image_preview_label.grid(row=14, column=0, pady=(0, 10), padx=10)
        self.upload_button = Button(self, text="Upload Image", command=self.upload_image)
        self.upload_button.grid(row=14, column=1, pady=(0, 10), padx=10, sticky="w")

    def reset_password(self):
        current_user = self.employee_business.current_user
        if not current_user or not getattr(current_user, "ID", None):
            Messagebox.show_error("Error", "No user loaded.")
            return

        new_pw = self.new_password_entry.get()
        confirm_pw = self.confirm_password_entry.get()

        if not new_pw:
            Messagebox.show_error("Error", "Please enter new password.")
            return
        if len(new_pw) < 6:
            Messagebox.show_error("Error", "Password must be at least 6 characters long:)")
            return
        if new_pw != confirm_pw:
            Messagebox.show_error("Error", "Passwords do not match.")
            return

        result = self.employee_business.update_employee_password(current_user.ID, new_pw)
        if result.success:
            self.new_password_entry.delete(0, "end")
            self.confirm_password_entry.delete(0, "end")
            Messagebox.show_info("Success", "Your password has been updated:)")
        else:
            Messagebox.show_error("Error", result.message)



    def set_current_user(self, user: Employee):
        self.employee_business.current_user = user
        current_user = self.employee_business.current_user
        if current_user:
            self.firstname_entry.delete(0,"end")
            self.firstname_entry.insert(0, current_user.FirstName)

            self.lastname_entry.delete(0,"end")
            self.lastname_entry.insert(0, current_user.LastName)

            self.Nationalcode_entry.delete(0,"end")
            self.Nationalcode_entry.insert(0, current_user.NationalCode)

            self.email_entry.delete(0,"end")
            self.email_entry.insert(0, current_user.Email)

            self.username_entry.delete(0,"end")
            self.username_entry.insert(0, current_user.UserName)

            self.employeestatus_entry.delete(0,"end")
            self.employeestatus_entry.insert(0, current_user.EmployeeStatusID)

            self.roleid_entry.delete(0,"end")
            self.roleid_entry.insert(0, current_user.RoleID)

        img_path = getattr(current_user, "ImagePath", None)
        if img_path:
            full_path = img_path if os.path.isabs(img_path) else os.path.join(os.getcwd(), img_path)
            if os.path.exists(full_path):
                try:
                    img = Image.open(full_path)
                    img.thumbnail((150, 150))
                    self._image_tk = ImageTk.PhotoImage(img)
                    self.image_preview_label.configure(image=self._image_tk, text="")
                except Exception:
                    self.image_preview_label.configure(image="", text="No image")
            else:
                self.image_preview_label.configure(image="", text="No image")
        else:
            self.image_preview_label.configure(image="", text="No image")

    def ensure_uploads_dir(self):
        uploads_dir = os.path.join(os.getcwd(), "uploads")
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)
        return uploads_dir

    def upload_image(self):
        current_user = self.employee_business.current_user
        if not current_user or not getattr(current_user, "ID", None):
            Messagebox.show_error("Error", "No user loaded.")
            return

        filetypes = [("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All files", "*.*")]
        src_path = filedialog.askopenfilename(title="Select an image", filetypes=filetypes)
        if not src_path:
            return

        try:
            uploads_dir = self.ensure_uploads_dir()
            ext = os.path.splitext(src_path)[1].lower()
            filename = f"user_{current_user.ID}_{int(time.time())}{ext}"
            dest_path = os.path.join(uploads_dir, filename)

            img = Image.open(src_path)
            img.thumbnail((800, 800))
            img.save(dest_path)

            relative_path = os.path.join("uploads", filename)
            result = self.employee_business.update_employee_image(current_user.ID, relative_path)
            if result.success:
                thumb = img.copy()
                thumb.thumbnail((150, 150))
                self._image_tk = ImageTk.PhotoImage(thumb)
                self.image_preview_label.configure(image=self._image_tk, text="")
                Messagebox.show_info("Success", "Image uploaded")
            else:
                Messagebox.show_error("Error", result.message)

        except Exception as e:
            Messagebox.show_error("Error", f"Failed to upload image: {str(e)}")

    def back_to_home(self):
        self.view_manager.show_frame("home")

    def load_employee(self, employee_id: int):
        result = self.employee_business.get_employee_by_id(employee_id)
        if result.success:
            self.employee_business.current_user = result.data
            self.set_current_user(self.employee_business.current_user)
        else:
            Messagebox.show_error("Error", result.message)

    def set_current_user_in_entries(self):

        self.firstname_entry.delete(0, "end")
        self.firstname_entry.insert(0, self.current_user.FirstName)

        self.lastname_entry.delete(0, "end")
        self.lastname_entry.insert(0, self.current_user.LastName)

        self.Nationalcode_entry.delete(0, "end")
        self.Nationalcode_entry.insert(0, self.current_user.NationalCode)

        self.email_entry.delete(0, "end")
        self.email_entry.insert(0, self.current_user.Email)

        self.username_entry.delete(0, "end")
        self.username_entry.insert(0, self.current_user.UserName)

        self.employeestatus_entry.delete(0, "end")
        self.employeestatus_entry.insert(0, self.current_user.EmployeeStatusID)

        self.roleid_entry.delete(0, "end")
        self.roleid_entry.insert(0, self.current_user.RoleID)





