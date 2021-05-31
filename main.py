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

class Simulador:
    def __init__(self):
        self.quantDentroReator = 0.0
        self.quantDentroDecantador = 0.0
        self.decantadorDisponivel = True
        self.quantDentroReator = 0.0
        self.quantDentroDecantador = 0.0
        self.quantOleo = 0.0
        self.quantNaOh = 0.0
        self.quantEtOh = 0.0
    # Tanque de oleo recebe oleo
    def tanqOlRec(self):
        self.quantOleo = 0.0
        while True:
        #     tanqueDeOleo.acquire()
        #     try:
            tempoReceb = random.randrange(1, 11)
            quantReceb = round(random.uniform(1,2), 2)
            self.quantOleo = round(self.quantOleo + quantReceb, 2)
            sleep(tempoReceb)
            print("Tanque de óleo recebeu", quantReceb, "litros - Total: ", self.quantOleo)
            # finally:
            #     tanqueDeOleo.release()
        
    def recebeNaOheEtOH(self):
        self.quantNaOh = 0.0
        self.quantEtOh = 0.0
        while True:
            self.quantNaOh += 0.25
            self.quantEtOh += 0.125
            sleep(1)
            print("Chegou NaOH e EtOH, quantidade de cada um: NaOH:", self.quantNaOh, "EtOH:", self.quantEtOh)
            

    def ativaReator(self):
        self.quantDentroReator = 0.0
        self.quantDentroDecantador = 0.0
        self.decantadorDisponivel = True
        while True:
            total = self.quantNaOh+self.quantEtOh+self.quantOleo
            print(total)
            if self.quantEtOh >= 5/2 and self.quantNaOh >= 5/4 and self.quantOleo >= 5/4 and self.decantadorDisponivel:
                if(total < 5):
                    if(self.quantDentroDecantador+total<=10):
                        self.quantDentroReator -= total
                        self.quantDentroDecantador += total
                        print("Decantador abastecido")
                        if(self.quantDentroDecantador==10):
                            self.decantadorDisponivel = False
                    else:
                        print("Decantador não consegue receber", total, "litros")
                if(total >= 5):
                    if(self.quantDentroDecantador+5<=10):
                        self.quantDentroReator -= 5
                        self.quantDentroDecantador += 5
                        print("Decantador abastecido")
                        if(self.quantDentroDecantador==10):
                            self.decantadorDisponivel = False
                    else:
                        print("Decantador não consegue receber 5 litros")
            else:
                ("Reator - Proporcao incorreta")
            sleep(1)

    def ativaDecantador(self):
        while True:
            if(self.quantDentroDecantador<10):
                self.decantadorDisponivel = True
                #Aguarda 2 segundos a saida do reator
                sleep(2)
            while self.quantDentroDecantador>=3:
                self.decantadorDisponivel = False

                print("Decantador trabalhando")
                self.quantDentroDecantador = self.quantDentroDecantador-3
                sleep(5)


simulador = Simulador()

t1 = Thread(target = simulador.tanqOlRec)
t1.start()

t2 = Thread(target= simulador.recebeNaOheEtOH)
t2.start()

t3 = Thread(target=simulador.ativaReator)
t3.start()

t4 = Thread(target=simulador.ativaDecantador)
t4.start()