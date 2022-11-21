# encode: utf-8
import cherrypy

WEB_ROOT = "/Users/pablotomasborda/Desktop/www.brainboost-limited.com/static/"
class CServer( object ) :
    @cherrypy.expose
    def do_contact(self, **params):
        pass
    @cherrypy.expose
    def enter_with_password(self,**params):
        with open("static/index.html", "r") as file:
            data = str(file.read())

        return data



cherrypy.quickstart(CServer(), '/',"cherrypy.cfg")