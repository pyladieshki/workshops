import cherrypy

def trythis():
    return "<html><body><h1>I am a simple function</h1></body></html>"
trythis.exposed = True

class SomeClass(object):

    def index(self):
        return "<html><body>I am an index method</body></html>"
    index.exposed = True

root = SomeClass()
root.trythis = trythis

if __name__ == '__main__':
    cherrypy.quickstart(root)	    
