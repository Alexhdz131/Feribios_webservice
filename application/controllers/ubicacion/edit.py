import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_ubicacion, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_ubicacion) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_ubicacion, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_ubicacion) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_ubicacion, **k):

    @staticmethod
    def POST_EDIT(id_ubicacion, **k):
        
    '''

    def GET(self, id_ubicacion, **k):
        message = None # Error message
        id_ubicacion = config.check_secure_val(str(id_ubicacion)) # HMAC id_ubicacion validate
        result = config.model.get_ubicacion(int(id_ubicacion)) # search for the id_ubicacion
        result.id_ubicacion = config.make_secure_val(str(result.id_ubicacion)) # apply HMAC for id_ubicacion
        return config.render.edit(result, message) # render ubicacion edit.html

    def POST(self, id_ubicacion, **k):
        form = config.web.input()  # get form data
        form['id_ubicacion'] = config.check_secure_val(str(form['id_ubicacion'])) # HMAC id_ubicacion validate
        # edit user with new data
        result = config.model.edit_ubicacion(
            form['id_ubicacion'],form['latitud'],form['longitud'],form['evento'],
        )
        if result == None: # Error on udpate data
            id_ubicacion = config.check_secure_val(str(id_ubicacion)) # validate HMAC id_ubicacion
            result = config.model.get_ubicacion(int(id_ubicacion)) # search for id_ubicacion data
            result.id_ubicacion = config.make_secure_val(str(result.id_ubicacion)) # apply HMAC to id_ubicacion
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/ubicacion') # render ubicacion index.html
