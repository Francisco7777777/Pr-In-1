from npc import NPC
 
'''
A classe "Guarda" ao receber como parâmetro a classe "NPC", passa ser uma
sub-classe (filha) da classe mãe "NPC".
A classe filha "Guarda" herdará o conteúdo da classe mãe.
'''
class Guarda(NPC):
   
    '''
    Ao declarar um construtor na subclasse, esse construtor irá sobrescrever
    O construtor da superclasse.
    '''
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 50
       
        # O método "super()" invoca um método ou parâmetro da classe mãe.
        super().__init__(nome, time, self.forca, self.municao)
      