from npc import NPC
 
'''
A classe "S_Elite" ao receber como parâmetro a classe "NPC", passa ser uma
sub-classe (filha) da classe mãe "NPC".
A classe filha "S_Elite" herdara o conteúdo da classe mãe.
'''
class S_Elite(NPC):
   
    '''
    Ao declarar um construtor na subclasse, esse construtor irá sobrescrever
    O construtor da superclasse.
    '''
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
       
        # O método "super()" invoca um método ou parâmetro da classe mãe.
        super().__init__(nome, time, self.forca, self.municao)
 
 
    def inf(self):
        super().infor()
