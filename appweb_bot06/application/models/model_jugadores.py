import config as config # Importa el archivo config

db = config.db # Crea un objeto DB del objeto DB creado en config

'''
Metodo para seleccionar todos los registros de la tabla jugadores
'''
def select_jugadores():
    try:
        return db.select('jugadores') # Selecciona todos los registros de la tabla jugadores
    except Exception as e:
        print "Model select_jugadores Error {}".format(e.args)
        print "Model select_jugadores Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el numero dado
'''

def select_numero(numero):
    try:
        return db.select('jugadores', where='numero=$numero', vars=locals())[0] # Selecciona el primer registro que coincida con el numero
    except Exception as e:
        print "Model select_numero Error {}".format(e.args)
        print "Model select_numero Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro usando numero, nombre, pais, posicion y equipo
'''
def insert_jugador(numero, nombre, pais, posicion, equipo):
    try:
        return db.insert('jugadores', numero=numero, nombre=nombre, pais=pais, posicion=posicion, equipo=equipo) # Inserta un registro en jugadores
    except Exception as e:
        print "Model insert_jugador Error {}".format(e.args)
        print "Model insert_jugador Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el numero recibido
'''
def delete_jugador(numero):
    try:
        return db.delete('jugadores', where='numero=$numero', vars=locals()) # Borra un registro de jugadores
    except Exception as e:
        print "Model delete_jugador Error {}".format(e.args)
        print "Model delete_jugador Message {}".format(e.message)
        return None

'''
Metodo para actualizar los campos en base al numero recibido
'''
def update_jugador(numero, nombre, pais, posicion, equipo): # Actualiza los campos de jugadores que coincidan con el numero
    try:
        return db.update('jugadores',
            nombre=nombre,
            pais=pais,
            posicion=posicion,
            equipo=equipo,
            where='numero=$numero',
            vars=locals())
    except Exception as e:
        print "Model update_jugadores Error {}".format(e.args)
        print "Model update_jugadores Message {}".format(e.message)
        return None
