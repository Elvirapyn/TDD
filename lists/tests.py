from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
# Create your tests here.
class HomePageTest(TestCase):
    # def test_root_url_resolve_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func,home_page)
    #
    def test_home_page_returns_coorect_html(self):
        response = self.client.get('/')
        #
        # html = response.content.decode('utf8')   #utf8解码后
        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>',html)
        # self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response,'home.html')

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
