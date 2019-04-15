import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_organizador, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_organizador) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_organizador, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_organizador) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_organizador, **k):

    @staticmethod
    def POST_DELETE(id_organizador, **k):
    '''

    def GET(self, id_organizador, **k):
        message = None # Error message
        id_organizador = config.check_secure_val(str(id_organizador)) # HMAC id_organizador validate
        result = config.model.get_organizadores(int(id_organizador)) # search  id_organizador
        result.id_organizador = config.make_secure_val(str(result.id_organizador)) # apply HMAC for id_organizador
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_organizador, **k):
        form = config.web.input() # get form data
        form['id_organizador'] = config.check_secure_val(str(form['id_organizador'])) # HMAC id_organizador validate
        result = config.model.delete_organizadores(form['id_organizador']) # get organizadores data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_organizador = config.check_secure_val(str(id_organizador))  # HMAC user validate
            id_organizador = config.check_secure_val(str(id_organizador))  # HMAC user validate
            result = config.model.get_organizadores(int(id_organizador)) # get id_organizador data
            result.id_organizador = config.make_secure_val(str(result.id_organizador)) # apply HMAC to id_organizador
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/organizadores') # render organizadores delete.html 
