import customtkinter as ctk
from source.utils.fade import fade_in, fade_out
from threading import Thread


def switch_theme(master, components):
    fade_out(master)
    switch = Thread(target=ctk.set_appearance_mode(components.switch_theme_mode.get()))
    switch.start()
    switch.join()
    components.btn_theme.configure(text=ctk.get_appearance_mode())
    master.favicon_changer()
    master.update()
    fade_in(master)


def off_value_theme():
    if ctk.get_appearance_mode() == "Dark":
        return "light"
    return "dark"

