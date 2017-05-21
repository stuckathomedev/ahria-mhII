import json

import cogs.voice.tts as tts
import cogs.chatterbot.chatter as chatter
import cogs.hotword.hotword as hotword
import cogs.journal.journal as journal
import cogs.weather.updated_weather as weather
from cogs.tweeter.tweeter import Tweeter
import cogs.task_manager.manager as manager
import cogs.task_manager.sms_manager as sms_manager

data = json.loads(open('data.json', 'r').read())
INDICOIO_API_KEY = "0115a1266812a351b9e80e72526916d9"

tweeter = Tweeter(data['twitter'], INDICOIO_API_KEY)

def dispatch_command(text: str):
    if text.startswith('tweet'):
        tweeter.tweet(text.lstrip())
    elif text.__contains__('the weather', 'send'):
        weather.send_text()
    elif text.__contains__('reminder', 'today'):

    elif text.__contains__('reminder', 'tomarrow'):

    elif text.__contains__('Search for'):

    elif                                                    



hotword.listen_forever(dispatch_command)

