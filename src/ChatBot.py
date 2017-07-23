import json
import sys

#Criando a classe
class ChatBot():
    
    def __init__(self, nome):
        try:
            memoria = open(nome + ".json", "r")
        except: 
            memoria = open(nome + ".json", "w")
            memoria.write('[["Felipe"], {"oi":"Olá, qual seu nome ?", "tchau":"tchau"}]')
            memoria.close()
            
            memoria = open(nome + ".json", "r")

        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None]

    def escuta(self, frase = None):
        if frase == None:
            frase = input(">: ")
        
        frase = str(frase)

        if 'executa' in frase:
            return frase

        frase = frase.lower()
        frase = frase.replace("é", "eh")

        return frase

    def pensa(self, frase):
       
        if frase in self.frases:
            return self.frases[frase]

        if frase == 'aprende':
            return 'digite a frase'
        
        # Reponde frases que dependem do histórico
        ultimaFrase = self.historico[-1]

        if ultimaFrase == "Olá, qual seu nome ?":
            nome = self.pegaNome(frase)
            resp = self.respondeNome(nome)
            return resp
        
        if ultimaFrase == "digite a frase":
            self.chave = frase
            return "digite a resposta"

        if ultimaFrase == 'digite a resposta':
            resp = frase 
            self.frases[self.chave] = resp 
            self.gravaMemoria()     
            return 'Aprendido'

        try:
            resp = str(eval(frase))
            return resp
        except:
            pass

        return "Não entendi"

    def pegaNome(self, nome):
        if 'o meu nome eh ' in nome:
            nome = nome[14:].lower()

        nome = nome.title()
        return nome

    #Função de boas-vindas
    def respondeNome(self, nome):
     
        if nome in self.conhecidos:
            frase = "Fala ae"
        else:
            frase = "Muito prazer"
            self.conhecidos.append(nome)

        return frase + " " + nome
    
    def gravaMemoria(self):
        memoria = open(self.nome + ".json", "w")
        json.dump([self.conhecidos, self.frases], memoria)
        memoria.close()

    def fala(self, frase):
        if 'executa ' in frase:
            plataforma = sys.platform
            comando = frase.replace('executa ', '')
            if 'win' in plataforma:
                import os
            elif 'linux' in plataforma:
                import subprocess as s
                try:
                    s.Popen(comando)
                except:
                    s.Popen(['xdg-open', comando])
        else:
            print(frase)
        self.historico.append(frase)

