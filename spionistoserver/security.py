from pyramid.security import Authenticated
from pyramid.security import Allow

__acl__ = [
        (Allow, Authenticated, 'View'),
        (Allow, 'group:administrators', 'Manage'),
    ]

USERS = {'fulano':'12345678',
          'mengano':'12345678'}
GROUPS = {'administrators':['group:administrators']}

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])