# Super classe (classe mãe):
class NPC:
    
    # Método construtor:
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def infor(self):
        print('Nome.....: ' + self.nome)
        print('Time.....: ' + str(self.time))
        print('Força....: ' + str(self.forca))
        print('Munição..: ' + str(self.municao))
        print('Vivo.....: ' + ('sim' if self.vivo else 'não'))
        print('Energia..: ' + str(self.energia))
        print('------------------------')
