from destino import Destino

class DestinoRepository:
    lista_destino: Destino = []

    def adicioanar_destino(self, destino:Destino):
        self.lista_destino.append(destino)

    def checa_se_destino_existe(self, ddd):
        for item in self.lista_destino:
            if item.DDD == ddd:
                return True
        return False

    def obter_destino_pelo_ddd(self, ddd):
        for item in self.lista_destino:
            if item.DDD == ddd:
                return item.Destino
        return None