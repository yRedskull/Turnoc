from datetime import datetime
from time import sleep as sl


def current_clock(components):
    now_clock_format = datetime.now().strftime("%H:%M:%S %d/%m/%y")

    components.now_clock.configure(text=now_clock_format)

    return components.now_clock.after(1000, lambda: current_clock(components))


def formater_clock(timestamp):
    clock = datetime.fromtimestamp(timestamp)
    clock_format = clock.strftime("%H:%M:%S %d/%m/%y")
    return clock_format


def add_seconds_in_timestamp_now(seconds):
    return datetime.timestamp(datetime.now()) + seconds


def shutdown_verification_clock(datetime_shutdown):
    return datetime.fromtimestamp(datetime_shutdown) <= datetime.now()

def seconds_for_shutdown(datetime_shutdown):
    return (datetime.fromtimestamp(datetime_shutdown) - datetime.now()).total_seconds()

def while_verification_shutdown(master, datetime_shutdown, components):
    ten_seconds = False
    
    while not shutdown_verification_clock(datetime_shutdown):
        if not components.shutdown_assert:
            break
        
        if not ten_seconds and seconds_for_shutdown(datetime_shutdown) < 11:
            master.open_countdown_popup(seconds_for_shutdown(datetime_shutdown))
            ten_seconds = True
            
        sl(1)
        
    return
        

