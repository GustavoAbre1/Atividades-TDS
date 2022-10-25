from destino_respository import DestinoRepository


class InterfaceUsuario:
    def __init__(self, destino_repository: DestinoRepository) -> None:
        self.destino_repository = destino_repository

    def solicitar_input_usuario(self):
        DDD = int(input("Digite o DDD:"))
        return DDD

    def exibir_destinos(self):
        formatText = "{0:<10} {1:<20}\n"
        menu = formatText.format("DDD", "destino")

        for item in self.destino_repository.lista_destino:
            menu += formatText.format(item.DDD, item.Destino)

        return menu


    def saida_usuario(self, DDD):
       if self.destino_repository.checa_se_destino_existe(DDD):
           return self.destino_repository.obter_destino_pelo_ddd(DDD)
       return "Destino não encontardo."


