from persistent import Persistent
from repoze.folder import Folder
from spionistoserver.security import __acl__

class SpionistoSite(Folder):
    __acl__ = __acl__
    
class Camera(Persistent):
    def __init__(self,data):
        self.data = data

def appmaker(zodb_root):
    if not 'spionisto' in zodb_root:
        app_root = SpionistoSite()
        camara1 = Camera('http://camara1/')
        app_root['camara1'] = camara1
        zodb_root['spionisto'] = app_root
        import transaction
        transaction.commit()
    return zodb_root['spionisto']