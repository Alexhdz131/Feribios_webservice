import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_oferta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_oferta) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_oferta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_oferta) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_oferta, **k):

    @staticmethod
    def POST_EDIT(id_oferta, **k):
        
    '''

    def GET(self, id_oferta, **k):
        message = None # Error message
        id_oferta = config.check_secure_val(str(id_oferta)) # HMAC id_oferta validate
        result = config.model.get_ofertas(int(id_oferta)) # search for the id_oferta
        result.id_oferta = config.make_secure_val(str(result.id_oferta)) # apply HMAC for id_oferta
        return config.render.edit(result, message) # render ofertas edit.html

    def POST(self, id_oferta, **k):
        form = config.web.input()  # get form data
        form['id_oferta'] = config.check_secure_val(str(form['id_oferta'])) # HMAC id_oferta validate
        # edit user with new data
        result = config.model.edit_ofertas(
            form['id_oferta'],form['descripcion'],form['puesto'],form['evento'],form['fecha'],form['hora'],
        )
        if result == None: # Error on udpate data
            id_oferta = config.check_secure_val(str(id_oferta)) # validate HMAC id_oferta
            result = config.model.get_ofertas(int(id_oferta)) # search for id_oferta data
            result.id_oferta = config.make_secure_val(str(result.id_oferta)) # apply HMAC to id_oferta
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/ofertas') # render ofertas index.html
