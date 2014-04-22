"""This example can handle the URIs
/    -> OnePage.index
/foo -> OnePage.foo -> foo
"""
import cherrypy

class App2:
    def index(self):
        return "this!"
    index.exposed = True

class OnePage(object):
    app2 = App2()

    def index(self):
        return "one page!"
    index.exposed = True


def foo():
    return 'Foo!'
foo.exposed = True

if __name__ == '__main__':
    root = OnePage()
    root.foo = foo
    #root.app2 = App2()
    cherrypy.quickstart(root)
