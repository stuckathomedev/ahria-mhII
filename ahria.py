import json
import re
import cogs.voice.tts as tts
import cogs.hotword.hotword as hotword
#import cogs.journal.journal as journal
import cogs.weather.updated_weather as weather
from cogs.tweeter.tweeter import Tweeter
#import cogs.task_manager.manager as manager
#import cogs.chatterbot.chatter as chatbot


data = json.loads(open('data.json', 'r').read())
INDICOIO_API_KEY = "0115a1266812a351b9e80e72526916d9"

tweeter = Tweeter(data['twitter'], INDICOIO_API_KEY)

tts.speak("Ahria initializing.")

def dispatch_command(text: str):
    if text.startswith('tweet'):
        tweeter.tweet(text.replace('tweet ', '', 1))
    elif text.__contains__('the weather'):
        m = re.search('(?:weather).+?([0-9]+)', text)
        weather.send_text(m.group(1), 'Boston, MA')

    elif text.__contains__('set a reminder for today at'):
        m = re.search('([0-9])\w* for (.*)'), text
        desc = m.group(2)
        phone_number = m.group(3)
        hour = m[0-1]
        minute = m[2-3]
        manager.manager_today(hour, minute, desc, phone_number)
    elif text.__contains__('set a reminder for tomorrow at'):
        m = re.search('([0-9])\w* for (.*?)'), text
        desc = m.group(2)
        phone_number = m.group(3)
        day = m[0]
        hour = m[1:2]
        minute = m[3:4]
        manager.manager_future(day, hour, minute, desc, phone_number)
    else:
        chatbot.enter_chatbot()

hotword.listen_forever(dispatch_command)

