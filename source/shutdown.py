import os
import subprocess

from tkinter.messagebox import showerror, showinfo, showwarning, askyesno
from source.clock import shutdown_clock


def shutdown_time(master, components, times, mode):
    final_times = dict()

    if not times or times == "0":
        return

    times = times.strip()

    match mode:
        case "Horas":
            final_times = {
                "seconds": calc_hour(int(times)),
                "mode": "Horas"
            }
        case "Minutos":
            final_times = {
                "seconds": calc_minutes(int(times)),
                "mode": "Minutos"
            }
        case "Segundos":
            final_times = {
                "seconds": int(times),
                "mode": "Segundos"
            }

    if final_times["seconds"] >= 315360000:
        return showerror(message="Tempo máximo atingido!!!\n(0 - 315359999 segundos -> 10 anos)")

    result = accept_timer(times, final_times)

    if not result:
        return

    try:
        command_exec(f"shutdown /s /t {final_times['seconds']}")

        components.btn_shutdown.configure(command=lambda: showwarning(message="Desligamento já agendado."))

        components.shutdown_assert = True
        components.final_times = final_times

        components.shutdown_clock.configure(text=shutdown_clock(components))
        components.label_shutdown_clock.place(relx=.1, y=45)
        components.shutdown_clock.place(relx=.3, y=45)
        components.btn_cancel.place(relx=.35, y=master.win_height-50)
    except Exception as e:
        showerror(message=e)


def accept_timer(times, final_times):
    mode = final_times["mode"]
    if int(times) == 1:
        mode = final_times["mode"][:-1]
    return askyesno(message=f"Deseja desligar o computador após {times} {mode}?",
                    icon="warning")


def cancel_shutdown(master, components):
    if not components.shutdown_assert:
        return False

    try:
        command_exec(f"shutdown /a")
        components.btn_cancel.place_forget()
        components.btn_shutdown.configure(command=lambda: shutdown_time(master, components, components.input_time.get(),
                                                                        components.combobox_mode.get()))
        components.shutdown_clock.place_forget()
        components.label_shutdown_clock.place_forget()
        showinfo(message="O desligamento foi cancelado!")
        components.shutdown_assert = False
        return True
    except Exception as e:
        showerror(message=e)


def command_exec(args):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    subprocess.Popen(args, startupinfo=startupinfo)


def calc_hour(hours):
    return hours * 3600


def calc_minutes(minutes):
    return minutes * 60
