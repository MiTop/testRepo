from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

def what_world(request):
	return Response('What willste %(ever)s!' % request.matchdict)

def gen_config():
    config = Configurator()
    gen_routeViews(config)
    return config

def gen_routeViews(config):
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    config.add_route('what', '/what/{ever}')
    config.add_view(what_world, route_name='what')

def initialize_server():
    config = gen_config()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    return server

#
# Start
#
if __name__ == '__main__':
    server = initialize_server()
    server.serve_forever()
   