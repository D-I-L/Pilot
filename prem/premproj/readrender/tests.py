from django.test import TestCase
from django.core.urlresolvers import resolve
#import pprint
from readrender.views import greet

# Create your tests here.
class ReadRenderTest(TestCase):
    #a simple control test that will pass always
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)
    
    def test_greet_url_resolves_to_greet_page_view(self):
        resp = resolve('/greet')  
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(resp)
        self.assertEqual(resp.func, greet)
        self.assertEqual(resp.url_name, 'greet')

    def test_read_url_resolves_to_read_page_view(self):
        resp = self.client.get('/read')
        self.assertEqual(resp.status_code, 200)
