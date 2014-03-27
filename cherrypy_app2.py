import cherrypy
import webcolors

class ColorsAndShapes:
    @cherrypy.expose
    def index(self):
        return "<html><body><h1>Welcome to our Shape&Color game!</h1>\
	        Please modify the URL to view a shape and a color as following\
		http://domainname:port/{circle, triangle, square}/color</body></html>"

    @cherrypy.expose
    def square(self, color="black"):
        return "<html><body><div style='background-color: " + color + ";\
                height: 200px; width: 200px;'></div></body></html>"    

    @cherrypy.expose
    def circle(self, color="black"):
        return "<html><body><div style='width: 200px;\
                height: 200px; border-radius: 100px; background-color:" + color +  ";\
                float: left;'></div></body></html>"

    @cherrypy.expose
    def triangle(self, color="black"):
        return "<html><body><div style='width: 0px; height: 0px;\
        border-style: solid; border-width: 0 100px 100px 100px;\
        border-color: transparent transparent" + webcolors.name_to_hex(color) + " transparent;\
        float: left;'></div></body></html>"

cherrypy.config.update({"server.socket_host": '0.0.0.0', "server.socket_port": 8090})
cherrypy.quickstart(ColorsAndShapes())
