"""
    Herança
"""
 
from guarda import Guarda
from soldado import Soldado
from elite import S_Elite
 
# Instalando os objetos.
s01 = Guarda('Tiro unico', 1)
s02 = Soldado('01', 2)
s03 = S_Elite('Fumaça', 1)
s04 = Guarda('Ninja', 2)
s05 = Soldado('05', 1)
s06 = S_Elite('mala', 2)
 
s02.vivo = False
s06.vivo = False
 
s01.infor()     # Chamando o método "infor()" da super classe (classe mãe).
s02.infor()
s03.inf()       # Chamando o método "inf()" da subclasse
s04.infor()
s05.infor()
s06.infor()
