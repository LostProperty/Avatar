from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound


# TODO: add homepage explaining what this is


def get_youtube_avatar(username):
    # https://gdata.youtube.com/feeds/api/users/peteygizzle?alt=json&fields=media:thumbnail
    return 'https://yt3.ggpht.com/-GrxiE3HZnjU/AAAAAAAAAAI/AAAAAAAAAAA/Ea6O-zeW4-8/s88-c-k-no/photo.jpg'


def hello_world(request):
    # TODO: rename function
    # TODO: dynamically get user name from the request. request.matchdict?
    avatar_url = get_youtube_avatar('peteygizzle')
    #return HTTPFound(location=avatar_url)
    return Response('Hello %(name)s!' % request.matchdict)


if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    # TODO: use watiress?
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings,)
    app = config.make_wsgi_app()
    return app
