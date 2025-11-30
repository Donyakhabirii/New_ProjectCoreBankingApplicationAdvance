#from tkinter import Tk
from ttkbootstrap import Window

class ApplicationWindow(Window):
    def __init__(self):
        super().__init__(themename = "darkly")
        self.title("Core Banking Application")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
    def resize(self,width, height):
        self.geometry(f"{width}x{height}")
    def show(self):
        self.mainloop()

    def change_theme(self, theme_name: str):
        self.style.theme_use(theme_name)
        for child in self.winfo_children():
            child.update_idletasks()
            try:
                child.tkraise()
            except Exception:
                pass