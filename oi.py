class Carro:
    def __init__(self,placa,modelo,ano):
        self.placa=placa 
        self.modelo=modelo
        self.ano=ano

if __name__=="__main__":
    palio=Carro("KJB-2668","EDX","1997")
    vectra=Carro("KIR-0932","Elite","2008")
    duster=Carro("\nOYW-4108","Dynamic","2015")
    print(palio.placa,vectra.placa,duster.placa)
    print(palio.modelo,vectra.modelo,duster.modelo)

    print(palio.ano,vectra.ano,duster.ano)          

def consumo(self):
    return f"{self.consumo}este e o consumo"
