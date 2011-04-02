from pyramid.view import view_config
from spionistoserver.models import MyModel

@view_config(context=MyModel, renderer='spionistoserver:templates/mytemplate.pt')
def my_view(request):
    return {'project':'spionisto.server'}
