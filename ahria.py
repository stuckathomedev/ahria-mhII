import json
from datetime import datetime
import re

import parsedatetime as pdt
import cogs.voice.tts as tts
import cogs.hotword.hotword as hotword
#import cogs.journal.journal as journal
import cogs.weather.weather as weather
from cogs.tweeter.tweeter import Tweeter
import cogs.task_manager.manager as manager
#import cogs.chatterbot.chatter as chatbot


data = json.loads(open('data.json', 'r').read())
INDICOIO_API_KEY = "0115a1266812a351b9e80e72526916d9"

tweeter = Tweeter(data['twitter'], INDICOIO_API_KEY)

tts.speak("Ahria initializing.")


def dispatch_command(text: str):
    print("Your response: " + text)
    text = text.lower()

    if text.startswith('tweet'):
        tweeter.tweet(text.replace('tweet ', '', 1))
    elif "weather" in text:
        # weather ... [phone number]
        m = re.search(r"(?:weather).+?\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})", text)
        if m is not None:
            weather.send_text(m.group(1) + m.group(2) + m.group(3), 'Boston, MA')
        else:
            tts.speak("Sorry, what was that you said about the weather?")
    elif text == "quit":
        tts.speak("Goodbye!")
        exit()
    elif "reminder" in text and "today" in text:
        desc_search = re.search(r"to ([A-Za-z0-9 ]+?)(?:for|at)", text)
        number_search = re.search(r"at (?:\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4}))(?:for|at|)", text)
        time_search = re.search(r"(?:at|on) ([APM :0-9]+)(?: |$)", text)

        if desc_search is not None and number_search is not None and time_search is not None:
            desc = desc_search.group(1)
            phone_number = number_search.group(1) + number_search.group(2) + number_search.group(3)
            human_time = time_search.group(1)

            cal = pdt.Calendar()
            time_struct, parse_status = cal.parse(human_time)
            dt = datetime(*time_struct[:6])
            manager.manager_today(dt.hour, dt.minute, desc, phone_number)
        else:
            tts.speak("Sorry, I didn't get that.")
    else:
        tts.speak("Sorry, I didn't understand that.")
    # elif "reminder" in text and "tomorrow" in text:
    #     m = re.search('([0-9])\w* for (.*?)', text)
    #     desc = m.group(2)
    #     phone_number = m.group(3)
    #     day = m[0]
    #     hour = m[1:2]
    #     minute = m[3:4]
    #     manager.manager_future(day, hour, minute, desc, phone_number)
    # else:
    #     chatbot.enter_chatbot()

hotword.listen_forever(dispatch_command)

