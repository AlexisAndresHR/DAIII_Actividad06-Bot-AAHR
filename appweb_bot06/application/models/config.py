import web
'''
Parametros de configuracion para conectarse a una base de datos MySQL o MariaDB
'''

db = web.database(
    dbn='mysql', # Motor de base de datos
    host='localhost', # Ruta del servidor
    db='fut_bot06', # Nombre de la Base de Datos
    user='futbot', # Usuario de la Base de Datos
    pw='futbot.2019', # Password del usuario
    port = 3306 # Puerto de MariaDB
    )
