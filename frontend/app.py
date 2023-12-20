from components import Components
from source.load_img import ImagesLoad

import customtkinter as ctk
from os import path


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

        match ctk.get_appearance_mode():
            case "Dark": self.wm_iconbitmap(self.images.logo_bitmap_light)
            case "Light": self.wm_iconbitmap(self.images.logo_bitmap_dark)

        ctk.set_default_color_theme(path.join(path.dirname(path.dirname(__file__)), "source", "assets", "themes",
                                    "dark_blue.json"))

        self.title("Turnoc")

        self.components = Components(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
