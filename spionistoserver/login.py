from pyramid.httpexceptions import HTTPFound

from pyramid.renderers import get_renderer
from pyramid.response import Response
from pyramid.security import forget
from pyramid.security import remember
from pyramid.url import resource_url
from pyramid.view import view_config

from spionistoserver.security import USERS

@view_config(context= 'spionistoserver.models.SpionistoSite',
             name= 'login',
             renderer= 'templates/login.pt')
@view_config(context = 'pyramid.exceptions.Forbidden',
             renderer= 'templates/login.pt')
def login(context,request):
    login_url = resource_url(request.root, request, 'login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/' # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    message = ''
    username = ''
    password = ''
    if 'form.submitted' in request.params:
        username = request.params['username']
        password = request.params['password']
        if USERS.get(username) == password:
            headers = remember(request, username)
            return HTTPFound(location = came_from,
                             headers = headers)
        message = 'Incorrect user name or password.'
        
    #Get master template
    master_template =  get_renderer('templates/master.pt').implementation()
    return dict(
        master_template = master_template,
        message = message,
        url = request.application_url + '/login',
        came_from = came_from,
        login = username,
        password = password,
        )

@view_config(context='spionistoserver.models.SpionistoSite', name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = resource_url(request.context, request),
                     headers = headers)