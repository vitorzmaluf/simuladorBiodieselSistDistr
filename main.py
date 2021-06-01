from threading import Thread
import random
from time import sleep
import math


class Simulador:
    def __init__(self):
        self.quantDentroReator = 0.0
        self.quantDentroDecantador = 0.0
        self.quantDentroReator = 0.0
        self.quantDentroDecantador = 0.0
        self.quantOleo = 0.0
        self.quantNaOh = 0.0
        self.quantEtOh = 0.0
        self.solLavagem = 0.0
        self.quantSecador = 0.0
        self.biodieselGerado = 0.0
        self.ciclosReator = 0
        self.quantGlicerina = 0.0

        self.rodando = True
        self.decantadorDisponivel = True
        self.lavadoresDisponiveis = True
        self.secadorDisponivel = True

        self.t1 = Thread(target = self.tanqOlRec)
        self.t2 = Thread(target= self.recebeNaOheEtOH)
        self.t3 = Thread(target=self.ativaReator)
        self.t4 = Thread(target=self.ativaDecantador)
        self.t5 = Thread(target=self.lavagem)
        self.t6 = Thread(target=self.secagem)

    # Tanque de oleo recebe oleo
    def tanqOlRec(self):
        self.quantOleo = 0.0
        while self.rodando:
            tempoReceb = random.randrange(1, 11)
            quantReceb = round(random.uniform(1,2), 2)
            self.quantOleo = round(self.quantOleo + quantReceb, 2)
            sleep(tempoReceb)
            print("Tanque de óleo recebeu", quantReceb, "litros - Total: ", self.quantOleo)
        
    def recebeNaOheEtOH(self):
        self.quantNaOh = 0.0
        self.quantEtOh = 0.0
        while self.rodando:
            self.quantNaOh += 0.25
            self.quantEtOh += 0.125
            sleep(1)
            print("Chegou NaOH e EtOH, quantidade de cada um: NaOH:", self.quantNaOh, "EtOH:", self.quantEtOh)
            

    def ativaReator(self):
        self.quantDentroReator = 0.0
        self.quantDentroDecantador = 0.0
        self.decantadorDisponivel = True
        while self.rodando:
            total = self.quantNaOh+self.quantEtOh+self.quantOleo
            if self.quantEtOh >= 5/2 and self.quantNaOh >= 5/4 and self.quantOleo >= 5/4 and self.decantadorDisponivel:
                if(self.quantDentroDecantador+5<=10):
                    self.quantDentroReator -= 5
                    self.quantEtOh -= 5/2
                    self.quantNaOh -= 5/4
                    self.quantOleo -= 5/4
                    self.quantDentroDecantador += 5
                    self.ciclosReator += 1
                    print("Decantador abastecido")
                    if(self.quantDentroDecantador==10):
                        self.decantadorDisponivel = False
                else:
                    print("Decantador não consegue receber 5 litros")
            else:
                ("Reator - Proporcao incorreta")
            sleep(1)

    def ativaDecantador(self):
        while self.rodando:
            if(self.quantDentroDecantador<10):
                self.decantadorDisponivel = True
                #Aguarda 2 segundos a saida do reator
                sleep(2)
            while self.quantDentroDecantador>=3:
                self.decantadorDisponivel = False

                print("Decantador trabalhando")
                self.quantGlicerina = self.quantGlicerina + (3*0.02)
                self.quantEtOh = self.quantEtOh + (3*0.09)
                if(self.lavadoresDisponiveis):
                    self.quantDentroDecantador = self.quantDentroDecantador-3
                    self.solLavagem += 3*0.89
                sleep(5)
    
    def lavagem(self):
        while self.rodando:
            if(self.solLavagem > 0 and self.lavadoresDisponiveis):
                self.lavadoresDisponiveis = False
                self.solLavagem = self.solLavagem*0.925
                self.solLavagem = self.solLavagem*0.925
                self.solLavagem = self.solLavagem*0.925
                self.quantSecador = self.solLavagem
                print("Foram lavados", self.solLavagem, "litros de solução")
                self.solLavagem = 0
                self.lavadoresDisponiveis = True
    
    def secagem(self):
        while self.rodando:
            if(self.quantSecador>0 and self.secadorDisponivel):
                self.quantSecador = self.quantSecador*0.97
                for i in range(0, int(math.ceil(self.quantSecador))):
                    sleep(5)
                    print("1 litro de solução foi secada")
                    self.quantSecador -= 1
                    self.biodieselGerado += 1
                    print("Total de Biodiesel gerado:", self.biodieselGerado)
                    
    def iniciar(self):
        self.t1.start()
        self.t2.start()
        self.t3.start()
        self.t4.start()
        self.t5.start()
        self.t6.start()

    def terminar(self):
        self.rodando = False
        sleep(5)
        print("Quantidade de Biodiesel produzido:", self.biodieselGerado)
        print("Quantidade de glicerina produzida:", self.quantGlicerina)
        print("Quantidade de Oleo restante:", self.quantOleo)
        print("Quantidade de NaOH restante:", self.quantNaOh)
        print("Quantidade de EtOH restante:", self.quantEtOh)
        print("Quantidade de ciclos do reator:", self.ciclosReator)
                


simulador = Simulador()
simulador.iniciar()
sleep(3200)
simulador.terminar()

