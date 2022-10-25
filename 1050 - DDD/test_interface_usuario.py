from destino import Destino
from interface_usuario import InterfaceUsuario
from destino_respository import DestinoRepository

def test_solicitar_input_usuario(monkeypatch):

    destino_respository = DestinoRepository()
    interface_usuario = InterfaceUsuario(destino_respository)
    monkeypatch.setattr('builtins.input', lambda _:75)
    DDD = interface_usuario.solicitar_input_usuario()

    assert DDD == 75

def test_saida_usuario():

    destino_respository = DestinoRepository
    interface_usuario = InterfaceUsuario(destino_respository)
    destino_respository.adicioanar_destino(Destino(75, "Feira de Santana"))

    assert interface_usuario.saida_usuario(75) == "Feira de Santana"






