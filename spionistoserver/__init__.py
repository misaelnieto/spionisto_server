from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from repoze.zodbconn.finder import PersistentApplicationFinder

from spionistoserver.models import appmaker
from spionistoserver.security import groupfinder

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    zodb_uri = settings.get('zodb_uri')
    if zodb_uri is None:
        raise ValueError("No 'zodb_uri' in application configuration.")

    finder = PersistentApplicationFinder(zodb_uri, appmaker)
    def get_root(request):
        return finder(request.environ)
    
    authentication_policy = AuthTktAuthenticationPolicy('vof5934d',
                                                        callback = groupfinder)
    authorization_policy = ACLAuthorizationPolicy()
    
    config = Configurator(root_factory=get_root, 
                          settings=settings,
                          authentication_policy = authentication_policy,
                          authorization_policy = authorization_policy)
    
    config.add_static_view('static', 'spionistoserver:static')
    config.scan('spionistoserver')
    return config.make_wsgi_app()
