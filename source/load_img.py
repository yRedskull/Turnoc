from customtkinter import CTkImage
from PIL import Image
from os import path


class ImagesLoad:
    def __init__(self):
        self.path_imgs = path.join(path.dirname(__file__), "assets", "img")
        self.logo_bitmap_dark = path.join(self.path_imgs, "favicon_dark.ico")
        self.logo_bitmap_light = path.join(self.path_imgs, "favicon_light.ico")
