import telepot
from ChatBot import ChatBot

telegram = telepot.Bot("API_KEY")
bot = ChatBot("Felipe")


def recebeMensagem(msg):
    frase = bot.escuta(frase = msg['text'])    
    resp = bot.pensa(frase)
    bot.fala(resp)
    #chatID = msg['chat']['id']
    tipoMsg, tipoChat, chatID = telepot.glance(msg) #Forma facilitada pela biblioteca do telepot
    telegram.sendMessage(chatID, resp)


telegram.message_loop(recebeMensagem)

while True:
    pass
