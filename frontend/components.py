import customtkinter as ctk

from source.validate import val_isnumber
from source.shutdown import shutdown_time, cancel_shutdown
from source.clock import current_clock

from source.utils.theme import off_value_theme, switch_theme


class Components:

    def __init__(self, master):
        self.master = master
        self.shutdown_assert = False
        self.final_times = None
        validate_input = master.register(val_isnumber)

        self.now_clock = ctk.CTkLabel(master, font=("Arial", 25), text_color=["#008800", "#00dd00"])
        current_clock(self)

        self.value_off = off_value_theme()
        self.switch_theme_mode = ctk.StringVar(value=ctk.get_appearance_mode())
        self.btn_theme = ctk.CTkSwitch(master, text=ctk.get_appearance_mode(), variable=self.switch_theme_mode,
                                       command=lambda: switch_theme(master, self),
                                       onvalue=ctk.get_appearance_mode(), offvalue=self.value_off)

        self.label_shutdown_clock = ctk.CTkLabel(master, text="Desligamento:", font=("Arial", 17),
                                                 text_color=["#EE44C2A", "#FF5D3B"])
        self.shutdown_clock = ctk.CTkLabel(master, font=("Arial", 25), text_color="#00aa00")

        self.input_time = ctk.CTkEntry(master, corner_radius=0, border_color="#000000", validate='key',
                                       validatecommand=(validate_input, '%P'))
        self.input_time.insert(0, "1")

        self.combobox_mode = ctk.CTkComboBox(master, values=["Horas", "Minutos", "Segundos"])
        self.combobox_mode.configure(state="readonly", dropdown_fg_color=["#ffffff", "#000000"])

        self.btn_shutdown = ctk.CTkButton(master, text="Temporizar desligamento",
                                          command=lambda: shutdown_time(master, self, self.input_time.get(),
                                                                        self.combobox_mode.get()),
                                          fg_color="#223344", border_color="#000000", border_width=1,
                                          hover_color="#000000")

        self.btn_cancel = ctk.CTkButton(master, text="Cancelar", fg_color="#223344", border_color="#000000",
                                        border_width=1,
                                        hover_color="#000000", command=lambda: cancel_shutdown(master, self))

        self.positions()

    def positions(self):
        self.btn_theme.place(relx=.83, y=5)
        self.now_clock.place(relx=.30, y=10)
        self.input_time.pack(expand=True, side=ctk.LEFT, padx=10)
        self.combobox_mode.pack(expand=True, side=ctk.LEFT, padx=10)
        self.btn_shutdown.pack(expand=True, side=ctk.LEFT, padx=10)
