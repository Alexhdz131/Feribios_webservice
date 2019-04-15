import web
import config

db = config.db


def get_all_organizadores():
    try:
        return db.select('organizadores')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_organizadores(id_organizador):
    try:
        return db.select('organizadores', where='id_organizador=$id_organizador', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_organizadores(id_organizador):
    try:
        return db.delete('organizadores', where='id_organizador=$id_organizador', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_organizadores(nombre,apellido_paterno,apellido_materno,empresa):
    try:
        return db.insert('organizadores',nombre=nombre,
apellido_paterno=apellido_paterno,
apellido_materno=apellido_materno,
empresa=empresa)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_organizadores(id_organizador,nombre,apellido_paterno,apellido_materno,empresa):
    try:
        return db.update('organizadores',id_organizador=id_organizador,
nombre=nombre,
apellido_paterno=apellido_paterno,
apellido_materno=apellido_materno,
empresa=empresa,
                  where='id_organizador=$id_organizador',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
