import os

from tkinter.messagebox import showerror, showinfo, showwarning, askyesno
try:
    from clock import shutdown_clock
except ImportError:
    from source.clock import shutdown_clock


def shutdown_time(master, components, times, mode):
    if not times or times == "0":
        return

    final_times = 0

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

    result = accept_timer(times, final_times)

    if not result:
        return

    try:
        os.system(f"shutdown /s /t {final_times['seconds']}")
        components.btn_shutdown.configure(command=lambda: showwarning(message="Desligamento já agendado."))

        components.shutdown_assert = True
        components.final_times = final_times

        components.shutdown_clock.configure(text=shutdown_clock(components))
        components.label_shutdown_clock.place(x=40, y=45)
        components.shutdown_clock.place(x=components.master.win_width/2.35, y=45)
        components.btn_cancel.place(x=master.win_width/2.6, y=master.win_height-50)
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
        return
    try:
        os.system(f"shutdown /a")
        components.btn_cancel.place_forget()
        components.btn_shutdown.configure(command=lambda: shutdown_time(master, components, components.input_time.get(),
                                                                        components.combobox_mode.get()))
        components.shutdown_clock.place_forget()
        components.label_shutdown_clock.place_forget()
        showinfo(title="Informação", message="O desligamento foi cancelado!")
    except Exception as e:
        showerror(title="Alert", message=e)


def calc_hour(hours):
    return hours * 3600


def calc_minutes(minutes):
    return minutes * 60
