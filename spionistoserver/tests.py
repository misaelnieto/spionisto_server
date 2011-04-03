import unittest

from pyramid import testing

class CameraTests(unittest.TestCase):
    def _getTargetClass(self):
        from spionistoserver.models import Camera
        return Camera

    def _makeOne(self, data = 'http://camarax/'):
        return self._getTargetClass()(data = data)
    
    def test_constructor(self):
        instance = self._makeOne()
        self.assertEqual(instance.data, 'http://camarax/')
        
def SpionistoSiteTests(self):
    def _getTargetClass(self):
        from spionistoserver.models import SpionistoSite
        return SpionistoSite

    def _makeOne(self):
        return self._getTargetClass()()
    
    def test_it(self):
        site = self._makeOne()
        self.assertEqual(site.__parent__, None)
        self.assertEqual(site.__name__, None)
    

class AppmakerTests(unittest.TestCase):

    def _callFUT(self, zodb_root):
        from spionistoserver.models import appmaker
        return appmaker(zodb_root)

    def test_no_app_root(self):
        root = {}
        self._callFUT(root)
        self.assertEqual(root['spionisto']['camara1'].data,
                         'http://camara1/')

    def test_w_app_root(self):
        app_root = object()
        root = {'spionisto': app_root}
        self._callFUT(root)
        self.failUnless(root['spionisto'] is app_root)
        

class MainViewTests(unittest.TestCase):
    def test_it(self):
        from spionistoserver.views import default_view
        context = testing.DummyResource()
        request = testing.DummyRequest()
        response = default_view(context, request)
        self.assertEqual(response.location, 'http://example.com/index')

