import os
import jinja2
import webapp2

# Jinja2 boilerplate
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class Handler(webapp2.RequestHandler):
    ''' Steve Huffman's convenient wrapper. '''

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


def handle_404(request, response, exception):
    ''' Custom 404 handler. '''
    template404 = jinja_env.get_template('404.html').render(relativePath=request.path)
    response.write(template404)
    response.set_status(404)


class MainPage(Handler):
    ''' Home page. '''
    def get(self):
        self.render("home.html")


class About(Handler):
    ''' About page. '''
    def get(self):
        self.render("about.html")


class Misc(Handler):
    '''Handles extra pages that don't fit anywhere else. '''

    def get(self, page):
        # listOfPages contains a list of template names from /templates/misc
        # e.g. listOfPages = ['noctis-terrain']
        listOfPages = []
        if page in listOfPages:
            self.render("misc/" + page + ".html")
        else:
            self.abort(404)


app = webapp2.WSGIApplication([(r'/', MainPage),
                               (r'/home', MainPage),
                               (r'/about', About),
                               (r'/misc/(.*)', Misc)
                               ],
                              debug=False)

app.error_handlers[404] = handle_404
