import cherrypy
import webcolors

class ColorsAndShapes:
    # index page
    @cherrypy.expose
    def index(self):
        return ("<html><body><h1>Welcome to our Shape&amp;Color game!</h1> "
                "Please modify the URL to view a shape and a color as "
                "following http://domainname:port/{circle, triangle, square}"
                "/color</body></html>")

    # square page
    @cherrypy.expose
    def square(self, color="black"):
        return ("<html><body><div style='background-color: {0};"
                "height: 200px; width: 200px;'></div>"
		"</body></html>").format(color)

    # circle page
    @cherrypy.expose
    def circle(self, color="black"):
        return ("<html><body><div style='width: 200px;"
                "height: 200px; border-radius: 100px;"
                "background-color: {0}; float: left;'>"
                "</div></body></html>").format(color)

    # triangle page
    @cherrypy.expose
    def triangle(self, color="black"):
        return ("<html><body><div style='width: 0; height: 0;"
                "border-style: solid; border-width: 0 100px 100px 100px;"
                "border-color: transparent transparent {0} transparent;"
                "float: left;'></div></body></html>").format(
                                 webcolors.name_to_hex(color))

cherrypy.config.update({"server.socket_host": '0.0.0.0', "server.socket_port": 8090})
cherrypy.quickstart(ColorsAndShapes())
