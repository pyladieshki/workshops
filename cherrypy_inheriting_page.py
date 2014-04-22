import cherrypy

# Tuikku Anttila 22.4.2014
# Tutorial 5 from the CherryPy package was used as a source

class Page(object):
    
    title = "Example Page"

    def header(self):
        return '''
        <html>
        <head>
        <title>%s</title>
        <head>
        <body><h2>%s</h2>

        ''' % (self.title, self.title)


    def footer(self):
        return '''
        </body>
        </html>
        '''

class MainPage(Page):

    title = "Main Page"

    def __init__(self):
        self.link = SecondPage()

    def index(self):
        return self.header() + "<p>Here's our page, and a link to</p> <a href='../link'>another page!</a>" + self.footer()

    index.exposed = True
    
    

class SecondPage(Page):

    def index(self):
        return self.header() + "<p> Another page! We didn't set a title in this class, so it is the same as in the base class.</p>" + "<a href='..'>Back</a>" + self.footer()
    index.exposed = True

cherrypy.quickstart(MainPage())
