import requests

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


def get_youtube_avatar_url(username):
    try:
        url = 'https://gdata.youtube.com/feeds/api/users/{0}?alt=json&fields=media:thumbnail'.format(username)
        response = requests.get(url)
        data = response.json()
        return data['entry']['media$thumbnail']['url']
    except:
        # Default profile picture
        return 'https://yt3.ggpht.com/-FN8ix3x-cCI/AAAAAAAAAAI/AAAAAAAAAAA/VK4OSAfDv3w/s77-c-k-no/photo.jpg'


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def home(request):
    return {}


@view_config(route_name='redirect_to_avatar')
def redirect_to_avatar(request):
    avatar_url = get_youtube_avatar_url(request.matchdict['username'])
    return HTTPFound(location=avatar_url)
