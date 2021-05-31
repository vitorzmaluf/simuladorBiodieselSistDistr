from threading import Thread, Lock
import random
from time import sleep


tanqueDeOleo = Lock()
tanqueNaOHeEtOH = Lock()
reator = Lock()
decantador = Lock()
tanqueLavagem1 = Lock()
tanqueLavagem2 = Lock()
tanqueLavagem3 = Lock()
secador = Lock()

# Tanque de oleo recebe oleo
def tanqOlRec():
    global quantOleo
    quantOleo = 0.0
    while True:
    #     tanqueDeOleo.acquire()
    #     try:
        tempoReceb = random.randrange(1, 11)
        quantReceb = round(random.uniform(1,2), 2)
        quantOleo = round(quantOleo + quantReceb, 2)
        sleep(tempoReceb)
        print("Tanque de óleo recebeu", quantReceb, "litros - Total: ", quantOleo)
        # finally:
        #     tanqueDeOleo.release()
    
def recebeNaOheEtOH():
    global quantNaOh, quantEtOh
    quantNaOh = 0.0
    quantEtOh = 0.0
    while True:
        quantNaOh += 0.25
        quantEtOh += 0.125
        sleep(1)
        print("Chegou NaOH e EtOH, quantidade de cada um: NaOH:", quantNaOh, "EtOH:", quantEtOh)
        

t1 = Thread(target = tanqOlRec)
t1.start()

t2 = Thread(target= recebeNaOheEtOH)
t2.start()