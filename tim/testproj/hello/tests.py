from django.test import TestCase


class HelloTestCase(TestCase):

    '''
    Test the page status and a variable (greet) in the response
    '''
    def test_page(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['greet'], 'hello')

    '''
    Test the status of a fictional page
    '''
    def test_page_not_found(self):
        resp = self.client.get('/xxx/')
        self.assertEqual(resp.status_code, 404)
