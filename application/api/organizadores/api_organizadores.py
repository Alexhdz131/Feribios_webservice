import web
import config
import json


class Api_organizadores:
    def get(self, id_organizador):
        try:
            # http://0.0.0.0:8080/api_organizadores?user_hash=12345&action=get
            if id_organizador is None:
                result = config.model.get_all_organizadores()
                organizadores_json = []
                for row in result:
                    tmp = dict(row)
                    organizadores_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(organizadores_json)
            else:
                # http://0.0.0.0:8080/api_organizadores?user_hash=12345&action=get&id_organizador=1
                result = config.model.get_organizadores(int(id_organizador))
                organizadores_json = []
                organizadores_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(organizadores_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            organizadores_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(organizadores_json)

# http://0.0.0.0:8080/api_organizadores?user_hash=12345&action=put&id_organizador=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,apellido_paterno,apellido_materno,empresa):
        try:
            config.model.insert_organizadores(nombre,apellido_paterno,apellido_materno,empresa)
            organizadores_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(organizadores_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_organizadores?user_hash=12345&action=delete&id_organizador=1
    def delete(self, id_organizador):
        try:
            config.model.delete_organizadores(id_organizador)
            organizadores_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(organizadores_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_organizadores?user_hash=12345&action=update&id_organizador=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_organizador, nombre,apellido_paterno,apellido_materno,empresa):
        try:
            config.model.edit_organizadores(id_organizador,nombre,apellido_paterno,apellido_materno,empresa)
            organizadores_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(organizadores_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            organizadores_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(organizadores_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_organizador=None,
            nombre=None,
            apellido_paterno=None,
            apellido_materno=None,
            empresa=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_organizador=user_data.id_organizador
            nombre=user_data.nombre
            apellido_paterno=user_data.apellido_paterno
            apellido_materno=user_data.apellido_materno
            empresa=user_data.empresa
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_organizador)
                elif action == 'put':
                    return self.put(nombre,apellido_paterno,apellido_materno,empresa)
                elif action == 'delete':
                    return self.delete(id_organizador)
                elif action == 'update':
                    return self.update(id_organizador, nombre,apellido_paterno,apellido_materno,empresa)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
