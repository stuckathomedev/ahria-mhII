from chatterbot import ChatBot


# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)


chatbot = ChatBot('Ahria', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
chatbot.train('chatterbot.corpus.english')

def enter_chatbot():
    while True:
        try:
            response = chatbot.get_response(None)

        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break