import web
import config
import json


class Api_ubicacion:
    def get(self, id_ubicacion):
        try:
            # http://0.0.0.0:8080/api_ubicacion?user_hash=12345&action=get
            if id_ubicacion is None:
                result = config.model.get_all_ubicacion()
                ubicacion_json = []
                for row in result:
                    tmp = dict(row)
                    ubicacion_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(ubicacion_json)
            else:
                # http://0.0.0.0:8080/api_ubicacion?user_hash=12345&action=get&id_ubicacion=1
                result = config.model.get_ubicacion(int(id_ubicacion))
                ubicacion_json = []
                ubicacion_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(ubicacion_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            ubicacion_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ubicacion_json)

# http://0.0.0.0:8080/api_ubicacion?user_hash=12345&action=put&id_ubicacion=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, latitud,longitud,evento):
        try:
            config.model.insert_ubicacion(latitud,longitud,evento)
            ubicacion_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ubicacion_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_ubicacion?user_hash=12345&action=delete&id_ubicacion=1
    def delete(self, id_ubicacion):
        try:
            config.model.delete_ubicacion(id_ubicacion)
            ubicacion_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ubicacion_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_ubicacion?user_hash=12345&action=update&id_ubicacion=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_ubicacion, latitud,longitud,evento):
        try:
            config.model.edit_ubicacion(id_ubicacion,latitud,longitud,evento)
            ubicacion_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ubicacion_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            ubicacion_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ubicacion_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_ubicacion=None,
            latitud=None,
            longitud=None,
            evento=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_ubicacion=user_data.id_ubicacion
            latitud=user_data.latitud
            longitud=user_data.longitud
            evento=user_data.evento
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_ubicacion)
                elif action == 'put':
                    return self.put(latitud,longitud,evento)
                elif action == 'delete':
                    return self.delete(id_ubicacion)
                elif action == 'update':
                    return self.update(id_ubicacion, latitud,longitud,evento)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
