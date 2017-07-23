
from ChatBot import ChatBot

Bot = ChatBot("Felipe")


while True:
    
    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)

    if resp == "tchau":
        break
