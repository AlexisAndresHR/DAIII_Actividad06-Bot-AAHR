import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, numero):
        jugador = config.model_jugadores.select_numero(numero) # Selecciona el registro que coincida con el numero
        return config.render.update(jugador) # Envia el registro y renderiza update.html

    def POST(self, nombre, pais, posicion, equipo):
        formulario = web.input() # Almacena los datos del formulario Web
        numero = formulario['numero'] # Almacena el numero escrito en el input
        nombre = formulario['nombre'] # Almacena el nombre escrito en el input
        pais = formulario['pais'] # Almacena el pais escrito en el input
        posicion = formulario['posicion'] # Almacena el posicion escrito en el input
        equipo = formulario['equipo'] # Almacena el equipo escrito en el input
        config.model_jugadores.update_jugador(numero, nombre, pais, posicion, equipo) # Actualiza los valores
        raise web.seeother('/') # Redirecciona al index.html
