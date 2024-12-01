import os, time
def desligar_uma_hora():
    os.system('shutdown /s /t 3600')

def desligar_meia_hora():
    os.system('shutdown /s /t 1800')    

def cancelar():
    os.system('shutdown /a')    


desligar_uma_hora()
desligar_meia_hora()
cancelar()    
cancelar()    