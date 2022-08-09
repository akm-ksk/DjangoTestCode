from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from snippets.views import top, snippet_new, snippet_detail, snippet_edit


# Create your tests here.
class CreateSnippetsTest(TestCase):
    def test_should(self):
        found = resolve('/snippets/new/')
        self.assertEqual(snippet_new, found.func)


class SnippetsDetailTest(TestCase):
    def test_should_resolve_snippet_detail(self):
        found = resolve('/snippets/1/')
        self.assertEqual(snippet_detail, found.func)


class EditSnippetsTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve('/snippets/1/edit/')
        self.assertEqual(snippet_edit, found.func)


class TopPageViewTest(TestCase):
    def CreateSnippetsTest(self):
        request = HttpRequest()
        # response = top(request)
        response = self.client.get('/')
        self.assertEqual(response.content, b'Hello World')

    def test_top_return_200(self):
        request = HttpRequest()  # リクエストのオブジェクトを生成
        # response = top(request)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        request = HttpRequest()
        # response = top(request)
        response = self.client.get('/')
        self.assertEqual(response.content, b'Hello World')
