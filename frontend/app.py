from time import sleep as sl
from frontend.components import Components
from source.load_img import ImagesLoad
from source.utils.fade import fade_out
from source.shutdown import cancel_shutdown
from tkinter.messagebox import askyesno
from tkinter import PhotoImage

from os import path
import customtkinter as ctk


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.images = ImagesLoad()

        # Resolution
        self.width_screen = self.winfo_screenwidth()
        self.height_screen = self.winfo_screenheight()
        self.win_width = 550
        self.win_height = 300
        width_plus = (self.width_screen // 2 - self.win_width // 2)
        height_plus = (self.height_screen // 2 - self.win_height // 2)
        self.geometry(f"{self.win_width}x{self.win_height}+{width_plus}+{height_plus}")
        self.resizable(False, False)

        self.favicon_changer()

        ctk.set_default_color_theme(path.join(path.dirname(path.dirname(__file__)), "source", "assets", "themes",
                                              "theme.json"))

        self.title("Turnoc")

        self.protocol("WM_DELETE_WINDOW", self.exit)

        self.components = Components(self)

    def favicon_changer(self):
        match ctk.get_appearance_mode():
            case "Dark":
                self.iconpath = self.images.logo_bitmap_light
                return self.wm_iconbitmap(self.images.logo_bitmap_light)
            case "Light":             
                self.iconpath = self.images.logo_bitmap_dark
                return self.wm_iconbitmap(self.images.logo_bitmap_dark)


    def open_countdown_popup(self, seconds_shutdown: int):
        popup = ctk.CTkToplevel(self)
        popup.title("Turnoc")

        # Resolution
        self.width_screen = self.winfo_screenwidth()
        self.height_screen = self.winfo_screenheight()
        win_width = 350
        win_height = 120
        width_plus = (self.width_screen // 2 - win_width // 2)
        height_plus = (self.height_screen // 2 - win_height // 2)
        popup.geometry(f"{win_width}x{win_height}+{width_plus}+{height_plus}")
        popup.resizable(False, False)
        popup.attributes("-topmost", True)
        
        popup.wm_iconbitmap(self.iconpath)

        lbl = ctk.CTkLabel(popup, text=f"Desligando em... {seconds_shutdown}", font=("Roboto", 32))
        lbl.pack(expand=True, pady=10)

        def safe_destroy():
            # tenta destruir, só se ainda existir
            if popup.winfo_exists():
                try:
                    popup.destroy()
                except Exception:
                    # proteger por via das dúvidas
                    pass

        while self.components.shutdown_assert:
            try: 
                if seconds_shutdown < 0:
                    popup.after(300, safe_destroy)
                    return
                
                lbl.configure(text=f"Desligando em... {seconds_shutdown:.0f}")
                popup.focus_force()

                seconds_shutdown -= 1
            except Exception:
                pass
            
            sl(1)

        
    def exit(self):
        resolution = askyesno(message="Gostaria de fechar o programa?")
        if not resolution:
            return

        fade_out(self)
        if self.components.shutdown_assert:
            cancel_shutdown(self, self.components)
        self.destroy()
