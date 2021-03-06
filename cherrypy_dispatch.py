#-*- coding: utf-8 -*-
import cherrypy

class Kid(object):

    @cherrypy.expose
    def index(self):
        return (u'<html><body><h1>Meet the child! '
                u'</h1></body></html>')
    @cherrypy.expose
    def future(self):
        return (u'<html><body><h1>Hi from the future! '
                u'I am a future child! ÖÖÖÖ'
                u'</h1></body></html>')

class Parent(object):
    child = Kid()

    @cherrypy.expose
    def index(self):
        return (u'<html><body><h1>hey there, '
                u'but I am a parent!</h1></body></html>')
    @cherrypy.expose
    def daughter(self):
	    return (u'<html><body><h1>Hey,'
	            u' I am a daughter!</h1></body></html>')
    
class Granny(object):

    @cherrypy.expose
    def index(self):
        return (u'<html><body><h1>hi, I am a '
                u'grandparent ;)</h1></body></html>')

if __name__ == '__main__':
    root = Granny()
    root.grandparent = Granny()
    root.grandparent.parent = Parent()
    #root.grandparent.parent.child = Kid()
    root.grandparent.parent.child.kiddo = Kid().future

    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})
    cherrypy.quickstart(root)
