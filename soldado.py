from npc import NPC
 
'''
A classe "Soldado" ao receber como parâmetro a classe "NPC", passa ser uma
sub-classe (filha) da classe mãe "NPC".
A classe filha "Soldado" herdara o conteúdo da classe mãe.
'''
class Soldado(NPC):
   
    '''
    Ao declarar um construtor na subclasse, esse construtor irá sobrescrever
    O construtor da superclasse.
    '''
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
       
        # O método "super()" invoca um método ou parâmetro da classe mãe.
        super().__init__(nome, time, self.forca, self.municao)
