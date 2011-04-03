from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.url import resource_url
from pyramid.view import view_config
from pyramid.response import Response

@view_config(context = 'spionistoserver.models.SpionistoSite',
             permission = 'View')
def default_view(context,request):
    return Response("Sitio de Spionisto")

@view_config(context = 'spionistoserver.models.Camera',
             permission = 'View')
def c_view(context,request):
    return Response("Camara1")