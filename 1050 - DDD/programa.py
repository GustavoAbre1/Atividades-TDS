from interface_usuario import InterfaceUsuario
from destino import Destino
from destino_respository import DestinoRepository

destino_repository = DestinoRepository()

destino_repository.adicioanar_destino(Destino(75, "Feira de Santana"))
destino_repository.adicioanar_destino(Destino(11, "São Paulo"))
destino_repository.adicioanar_destino(Destino(31, "Belo Horizonte"))
destino_repository.adicioanar_destino(Destino(92, "Amazonas"))

interface_usuario = InterfaceUsuario(destino_repository)

print(interface_usuario.exibir_destinos())

while True:
    DDD = interface_usuario.solicitar_input_usuario()
    print(interface_usuario.saida_usuario(DDD))




