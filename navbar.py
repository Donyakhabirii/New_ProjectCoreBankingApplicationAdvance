from ttkbootstrap import Frame, Checkbutton
from ttkbootstrap.style import LIGHT, TOGGLE

class NavbarFrame(Frame):
    def __init__(self, window, view_manager):
        super().__init__(window)
        self.view_manager = view_manager

        self.theme_checkbutton = Checkbutton(self,text="Dark",bootstyle="light-round-toggle",command=self.toggle_theme)
        self.theme_checkbutton.grid(row=0, column=0, pady=10, padx=10)

    def toggle_theme(self):
        if self.theme_checkbutton.instate(['selected']):
            self.view_manager.set_theme("cosmo")
            self.theme_checkbutton.config(text="Light")
        else:
            self.view_manager.set_theme("darkly")
            self.theme_checkbutton.config(text="Dark")
