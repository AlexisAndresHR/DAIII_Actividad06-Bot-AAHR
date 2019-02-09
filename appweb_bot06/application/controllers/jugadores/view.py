import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, numero):
        jugador = config.model_jugadores.select_numero(numero) # Selecciona el registro que coincida con el numero
        return config.render.view(jugador) # Envia el registro y renderiza view.html
