from modules import Casa
from modules import Pessoa

casa_ana = Casa()
ana = Pessoa('Ana')

ana.set_local(casa_ana)
casa_ana.set_proprietario(ana)

proprietario = casa_ana.get_proprietario()
proprietario.se_apresentar()
