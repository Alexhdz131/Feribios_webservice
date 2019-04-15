import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_oferta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_oferta) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_oferta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_oferta) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_oferta, **k):

    @staticmethod
    def POST_DELETE(id_oferta, **k):
    '''

    def GET(self, id_oferta, **k):
        message = None # Error message
        id_oferta = config.check_secure_val(str(id_oferta)) # HMAC id_oferta validate
        result = config.model.get_ofertas(int(id_oferta)) # search  id_oferta
        result.id_oferta = config.make_secure_val(str(result.id_oferta)) # apply HMAC for id_oferta
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_oferta, **k):
        form = config.web.input() # get form data
        form['id_oferta'] = config.check_secure_val(str(form['id_oferta'])) # HMAC id_oferta validate
        result = config.model.delete_ofertas(form['id_oferta']) # get ofertas data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_oferta = config.check_secure_val(str(id_oferta))  # HMAC user validate
            id_oferta = config.check_secure_val(str(id_oferta))  # HMAC user validate
            result = config.model.get_ofertas(int(id_oferta)) # get id_oferta data
            result.id_oferta = config.make_secure_val(str(result.id_oferta)) # apply HMAC to id_oferta
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/ofertas') # render ofertas delete.html 
