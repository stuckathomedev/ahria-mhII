import cogs
from datetime import datetime
from threading import Timer


def return_second_today(hour : int, minute: int):
    x = datetime.today()
    y = x.replace(hour=hour, minute=minute)
    delta_t = y - x

    secs = delta_t.seconds + 1
    return secs


def manager_timer(seconds : int):
    t = Timer(seconds, times_up)
    t.start()


def times_up():
    print("You have an event soon!: ")


def manager_today(hour : int, minute : int):
    total_seconds = return_second_today(hour, minute)
    manager_timer(total_seconds)


manager_today(2, 46)