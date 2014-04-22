import cherrypy
from mako.template import Template

class PersonalInfo(object):

    @cherrypy.expose	
    def index(self, name=u'anonymous'):
        template = Template(filename="personalinfo.html")
        return template.render(name=name)

    @cherrypy.expose
    def multiply(self, *args):
        mult = 1
        for arg in args:
            mult = mult * int(arg)
        template = Template(filename="multiplication.html")
        return template.render(result=mult)

root = PersonalInfo()

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(root)
