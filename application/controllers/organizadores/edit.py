import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_organizador, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_organizador) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_organizador, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_organizador) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_organizador, **k):

    @staticmethod
    def POST_EDIT(id_organizador, **k):
        
    '''

    def GET(self, id_organizador, **k):
        message = None # Error message
        id_organizador = config.check_secure_val(str(id_organizador)) # HMAC id_organizador validate
        result = config.model.get_organizadores(int(id_organizador)) # search for the id_organizador
        result.id_organizador = config.make_secure_val(str(result.id_organizador)) # apply HMAC for id_organizador
        return config.render.edit(result, message) # render organizadores edit.html

    def POST(self, id_organizador, **k):
        form = config.web.input()  # get form data
        form['id_organizador'] = config.check_secure_val(str(form['id_organizador'])) # HMAC id_organizador validate
        # edit user with new data
        result = config.model.edit_organizadores(
            form['id_organizador'],form['nombre'],form['apellido_paterno'],form['apellido_materno'],form['empresa'],
        )
        if result == None: # Error on udpate data
            id_organizador = config.check_secure_val(str(id_organizador)) # validate HMAC id_organizador
            result = config.model.get_organizadores(int(id_organizador)) # search for id_organizador data
            result.id_organizador = config.make_secure_val(str(result.id_organizador)) # apply HMAC to id_organizador
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/organizadores') # render organizadores index.html
