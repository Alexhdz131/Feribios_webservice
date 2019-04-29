import web
import config

db = config.db


def get_all_ubicacion():
    try:
        return db.select('ubicacion')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_ubicacion(id_ubicacion):
    try:
        return db.select('ubicacion', where='id_ubicacion=$id_ubicacion', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_ubicacion(id_ubicacion):
    try:
        return db.delete('ubicacion', where='id_ubicacion=$id_ubicacion', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_ubicacion(latitud,longitud,evento):
    try:
        return db.insert('ubicacion',latitud=latitud,
longitud=longitud,
evento=evento)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_ubicacion(id_ubicacion,latitud,longitud,evento):
    try:
        return db.update('ubicacion',id_ubicacion=id_ubicacion,
latitud=latitud,
longitud=longitud,
evento=evento,
                  where='id_ubicacion=$id_ubicacion',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
