from datetime import datetime


def current_clock(components):
    now_clock_format = datetime.now().strftime("%H:%M:%S")

    components.now_clock.configure(text=now_clock_format)

    return components.now_clock.after(1000, lambda: current_clock(components))


def shutdown_clock(components):
    clock = datetime.fromtimestamp(datetime.timestamp(datetime.now()) + components.final_times["seconds"])
    clock_format = clock.strftime("%H:%M:%S %d/%m/%y")
    return clock_format

