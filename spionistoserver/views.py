from pyramid.view import view_config
from pyramid.response import Response
from pyramid.renderers import get_renderer

@view_config(context = 'spionistoserver.models.SpionistoSite',
             renderer = 'templates/site_root.pt',
             permission = 'View')
def site_root_view(context,request):
    #Get master template
    master_template =  get_renderer('templates/master.pt').implementation()
    return dict (master_template = master_template,)

@view_config(context = 'spionistoserver.models.Camera',
             permission = 'View')
def default_camera_view(context,request):
    return Response("Esta es la Camara 1")

    