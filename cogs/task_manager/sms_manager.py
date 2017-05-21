import cogs
from cogs.task_manager.manager import rem_desc'
import twilio.rest
import pyowm
from pyowm import OWM
from twilio.rest import Client


def send_text(phone_number):

    global rem_desc
    notification = "Recent notification: " + rem_desc

    account_sid = "AC984fee9fe6cc06c84923b4466a0c99a6"
    auth_token = "f107dd35e35b59857bbe03917ee1f83e"
    client = Client(account_sid, auth_token)

    message = client.api.account.messages.create(to="+1" + phone_number,
                                                 from_="+19788493104 ",
                                                 body= notification)

send_text("9788448697")
