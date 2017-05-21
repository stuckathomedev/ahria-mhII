import cogs
from datetime import datetime
from threading import Timer
from cogs.task_manager.sms_manager import send_text

rem_desc = ""

def return_second_today(hour : int, minute: int):
    x = datetime.today()
    y = x.replace(hour=hour, minute=minute)
    delta_t = y - x

    secs = delta_t.seconds + 1
    return secs


def manager_timer(seconds : int):
    t = Timer(seconds, times_up)
    t.start()

def notification_timer(seconds : int):
    t = Timer(seconds, send_text)
    t.start()

def times_up():
    print("You have an event soon!: " + rem_desc)


def manager_today(hour : int, minute : int, desc : str):
    total_seconds = return_second_today(hour, minute)
    global rem_desc
    rem_desc = desc
    manager_timer(total_seconds)
    notification_timer(total_seconds)


manager_today(3, 43, "Kill Kunal")