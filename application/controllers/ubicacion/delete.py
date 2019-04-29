import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_ubicacion, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_ubicacion) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_ubicacion, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_ubicacion) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_ubicacion, **k):

    @staticmethod
    def POST_DELETE(id_ubicacion, **k):
    '''

    def GET(self, id_ubicacion, **k):
        message = None # Error message
        id_ubicacion = config.check_secure_val(str(id_ubicacion)) # HMAC id_ubicacion validate
        result = config.model.get_ubicacion(int(id_ubicacion)) # search  id_ubicacion
        result.id_ubicacion = config.make_secure_val(str(result.id_ubicacion)) # apply HMAC for id_ubicacion
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_ubicacion, **k):
        form = config.web.input() # get form data
        form['id_ubicacion'] = config.check_secure_val(str(form['id_ubicacion'])) # HMAC id_ubicacion validate
        result = config.model.delete_ubicacion(form['id_ubicacion']) # get ubicacion data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_ubicacion = config.check_secure_val(str(id_ubicacion))  # HMAC user validate
            id_ubicacion = config.check_secure_val(str(id_ubicacion))  # HMAC user validate
            result = config.model.get_ubicacion(int(id_ubicacion)) # get id_ubicacion data
            result.id_ubicacion = config.make_secure_val(str(result.id_ubicacion)) # apply HMAC to id_ubicacion
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/ubicacion') # render ubicacion delete.html 
