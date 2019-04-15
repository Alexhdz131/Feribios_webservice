import web
import config
import json


class Api_ofertas:
    def get(self, id_oferta):
        try:
            # http://0.0.0.0:8080/api_ofertas?user_hash=12345&action=get
            if id_oferta is None:
                result = config.model.get_all_ofertas()
                ofertas_json = []
                for row in result:
                    tmp = dict(row)
                    ofertas_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(ofertas_json)
            else:
                # http://0.0.0.0:8080/api_ofertas?user_hash=12345&action=get&id_oferta=1
                result = config.model.get_ofertas(int(id_oferta))
                ofertas_json = []
                ofertas_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(ofertas_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            ofertas_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ofertas_json)

# http://0.0.0.0:8080/api_ofertas?user_hash=12345&action=put&id_oferta=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, descripcion,puesto,evento,fecha,hora):
        try:
            config.model.insert_ofertas(descripcion,puesto,evento,fecha,hora)
            ofertas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ofertas_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_ofertas?user_hash=12345&action=delete&id_oferta=1
    def delete(self, id_oferta):
        try:
            config.model.delete_ofertas(id_oferta)
            ofertas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ofertas_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_ofertas?user_hash=12345&action=update&id_oferta=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_oferta, descripcion,puesto,evento,fecha,hora):
        try:
            config.model.edit_ofertas(id_oferta,descripcion,puesto,evento,fecha,hora)
            ofertas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ofertas_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            ofertas_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ofertas_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_oferta=None,
            descripcion=None,
            puesto=None,
            evento=None,
            fecha=None,
            hora=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_oferta=user_data.id_oferta
            descripcion=user_data.descripcion
            puesto=user_data.puesto
            evento=user_data.evento
            fecha=user_data.fecha
            hora=user_data.hora
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_oferta)
                elif action == 'put':
                    return self.put(descripcion,puesto,evento,fecha,hora)
                elif action == 'delete':
                    return self.delete(id_oferta)
                elif action == 'update':
                    return self.update(id_oferta, descripcion,puesto,evento,fecha,hora)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
