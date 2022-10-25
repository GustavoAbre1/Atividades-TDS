from destino_respository import DestinoRepository
from destino import Destino

def test_checa_se_destino_existe():

    destino_respository = DestinoRepository()
    destino_respository.adicioanar_destino(Destino(75, "Feira de Santana"))

    assert destino_respository.checa_se_destino_existe(75)

def test_obter_destino_pelo_ddd():

    destino_respository = DestinoRepository()
    destino_respository.adicioanar_destino(Destino(71, "Belo Horizonte"))
    destino_respository.obter_destino_pelo_ddd(71)

    assert destino_respository.obter_destino_pelo_ddd(71) == "Belo Horizonte"