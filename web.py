import cherrypy
import Stoker
import os

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        s = Stoker.Stoker("192.168.1.91")
        s.setup()

        self.stoker = s
        return open('index.html')

    @cherrypy.expose
    def getSmokerTemp(self):
        return str(self.stoker.sensors[0].currentTemp)

    @cherrypy.expose
    def getTargetTemp(self):
        return str(self.stoker.sensors[0].targetTemp)

    @cherrypy.expose
    def getFoodTemp(self):
        return str(self.stoker.sensors[1].currentTemp)

    @cherrypy.expose
    def getBlowerStatus(self):
        if self.stoker.blowers[0].on == 0:
            return "OFF"
        else:
            return "ON"

    @cherrypy.expose
    def setTargetTemp(self, target):
        self.stoker.sensors[0].set_target_temp(int(target))


if __name__ == '__main__':

    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    webapp = StringGenerator()
    cherrypy.quickstart(webapp, '/', conf)
