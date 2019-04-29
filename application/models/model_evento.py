import web
import config

db = config.db


def get_all_evento():
    try:
        return db.select('evento')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_evento(id_evento):
    try:
        return db.select('evento', where='id_evento=$id_evento', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_evento(id_evento):
    try:
        return db.delete('evento', where='id_evento=$id_evento', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_evento(titulo,descripcion,fecha,hora,ubicacion,organizador):
    try:
        return db.insert('evento',titulo=titulo,
descripcion=descripcion,
fecha=fecha,
hora=hora,
ubicacion=ubicacion,
organizador=organizador)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_evento(id_evento,titulo,descripcion,fecha,hora,ubicacion,organizador):
    try:
        return db.update('evento',id_evento=id_evento,
titulo=titulo,
descripcion=descripcion,
fecha=fecha,
hora=hora,
ubicacion=ubicacion,
organizador=organizador,
                  where='id_evento=$id_evento',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
