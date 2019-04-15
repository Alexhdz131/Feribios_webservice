import web
import config

db = config.db


def get_all_ofertas():
    try:
        return db.select('ofertas')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_ofertas(id_oferta):
    try:
        return db.select('ofertas', where='id_oferta=$id_oferta', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_ofertas(id_oferta):
    try:
        return db.delete('ofertas', where='id_oferta=$id_oferta', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_ofertas(descripcion,puesto,evento,fecha,hora):
    try:
        return db.insert('ofertas',descripcion=descripcion,
puesto=puesto,
evento=evento,
fecha=fecha,
hora=hora)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_ofertas(id_oferta,descripcion,puesto,evento,fecha,hora):
    try:
        return db.update('ofertas',id_oferta=id_oferta,
descripcion=descripcion,
puesto=puesto,
evento=evento,
fecha=fecha,
hora=hora,
                  where='id_oferta=$id_oferta',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
