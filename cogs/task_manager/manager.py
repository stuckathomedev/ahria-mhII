from datetime import datetime
from threading import Timer
from twilio.rest import Client

rem_desc = ""
phone_number = ""

def return_second_today(hour : int, minute: int):
    x = datetime.today()
    y = x.replace(hour=hour, minute=minute)
    delta_t = y - x

    secs = delta_t.seconds + 1
    return secs


def return_second_future(day : int, hour : int, minute : int):
    x = datetime.today()
    y = x.replace(day=day, hour=hour, minute=minute)
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

def send_text():

    global rem_desc
    notification = "The recent notification: " + rem_desc

    global phone_number

    account_sid = "AC984fee9fe6cc06c84923b4466a0c99a6"
    auth_token = "f107dd35e35b59857bbe03917ee1f83e"
    client = Client(account_sid, auth_token)

    message = client.api.account.messages.create(to="+1" + phone_number,
                                                 from_="+19788493104 ",
                                                 body= notification)


def manager_today(hour : int, minute : int, desc : str, phone_num : str):
    total_seconds = return_second_today(hour, minute)
    global rem_desc
    rem_desc = desc
    global phone_number
    phone_number = phone_num
    manager_timer(total_seconds)
    notification_timer(total_seconds)


def manager_future(day : int, hour : int, minute : int, desc : str, phone_num : str):
    total_seconds = return_second_future(day, hour, minute)
    global rem_desc
    rem_desc = desc
    global phone_number
    phone_number = phone_num
    manager_timer(total_seconds)
    notification_timer(total_seconds)


manager_today(4, 18, "Kill Kunal", "9788448697")

