from pyramid.view import view_config
from pyramid.response import Response

@view_config(context = 'spionistoserver.models.SpionistoSite',
             permission = 'View')
def default_view(context,request):
    return Response("Bienvenido a Spionisto server")

@view_config(context = 'spionistoserver.models.Camera',
             permission = 'View')
def c_view(context,request):
    return Response("Esta es la Camara 1")

    