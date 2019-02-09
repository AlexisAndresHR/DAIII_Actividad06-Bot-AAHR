import web # Importa la libreria web.py
import application.models.model_jugadores as model_jugadores # Importa el modelo_jugadores


render = web.template.render('application/views/jugadores/', base='master') # Configura la ubicacion de las vistas