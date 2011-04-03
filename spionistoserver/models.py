from persistent import Persistent
from persistent.mapping import PersistentMapping

class SpionistoSite(PersistentMapping):
    __name__ = None
    __parent__ = None

class Camera(Persistent):
    def __init__(self,data):
        self.data = data

def appmaker(zodb_root):
    if not 'spionisto' in zodb_root:
        app_root = SpionistoSite()
        camara1 = Camera('http://camara1/')
        app_root['camara1'] = camara1
        camara1.__name__ = 'Camara1'
        camara1.__parent__ = app_root
        zodb_root['spionisto'] = app_root
        import transaction
        transaction.commit()
    return zodb_root