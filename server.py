# encode: utf-8
import cherrypy

WEB_ROOT = "/root/www.brainboost-limited.com/static"
class CServer( object ) :
    @cherrypy.expose
    def do_contact(self, **params):
        pass
    @cherrypy.expose
    def enter_with_password(self,**params):
        if params['pwd']=='probando':
            with open("static/index.html", "r") as file:
                data = str(file.read())

            return data
        else:
            return 'False'


cherrypy.quickstart(CServer(), '/',"cherrypy.cfg")