import cherrypy

class App1:
    def index(self):
        return u"My first app"
    index.exposed = True

    @cherrypy.expose
    def apples(self):
	return "<html><body><h1 style='color: red; text-align: center;'>Apples! Yum :) </h1></body></html>"

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    # 1. mount the given root 
    # 2. start the builtin server (and engine)
    # 3. block
    cherrypy.quickstart(App1())
