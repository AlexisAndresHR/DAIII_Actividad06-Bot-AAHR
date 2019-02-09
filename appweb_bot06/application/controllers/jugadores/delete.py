import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, numero):
        jugadores = config.model_jugadores.select_numero(numero) # Selecciona el registro que coincida con numero
        return config.render.delete(jugadores) # Envia el registro y renderiza delete.html

    def POST(self, numero):
        formulario = web.input() # Crea un objeto formulario con los datos enviados con el formulario
        numero = formulario['numero'] # Obtiene el numero almacenado en el formulario
        config.model_jugadores.delete_jugador(numero) # Borra el registro del numero seleccionado
        raise web.seeother('/') # Renderiza a raiz
