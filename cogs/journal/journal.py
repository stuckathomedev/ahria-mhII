from datetime import datetime
import json

import indicoio


def add_entry(text, indicoio_api_key):
    indicoio.config.api_key = indicoio_api_key
    try:
        entries = json.loads(open("journal.json", "r").read())
    except json.JSONDecodeError:
        entries = []
    entries.append(
        {'date': datetime.utcnow(), 'keywords': indicoio.keywords(text)})
    open("journal.json", "w").write(json.dumps(entries))