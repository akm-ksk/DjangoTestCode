from django.http import HttpRequest
from django.test import TestCase, Client, RequestFactory
from django.urls import resolve
from django.contrib.auth import get_user_model

from snippets.views import top, snippet_new, snippet_detail, snippet_edit
from snippets.models import Snippet

UserModel = get_user_model()


# Create your tests here.
# class TopPageViewTest(TestCase):
#     def CreateSnippetsTest(self):
#         # request = HttpRequest()
#         # response = top(request)
#         response = self.client.get('/')
#         self.assertEqual(response.content, b'Hello World')
#
#     def test_top_return_200(self):
#         # request = HttpRequest()  # リクエストのオブジェクトを生成
#         # response = top(request)
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_top_returns_expected_content(self):
#         # request = HttpRequest()
#         # response = top(request)
#         response = self.client.get('/')
#         self.assertEqual(response.content, b'Hello World')

class TopPageTest(TestCase):
    def test_top_page_returns_200_and_expected_title(self):
        response = self.client.get('/')
        self.assertContains(response, 'Djangoスニペット', status_code=200)

    def test_top_page_uses_expected_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'snippets/top.html')


class TopPageRenderSnippetsTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username='test_user',
            email='test@example.com',
            password='top_secret_pass0001',
        )
        self.snippets = Snippet.objects.create(
            title='title01',
            code='print("Hellow")',
            description='description1',
            create_by=self.user,
        )

    def test_should_return_snippet_title(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.snippets.title)

    def test_should_return_username(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)


# class CreateSnippetsTest(TestCase):
#     def test_should(self):
#         found = resolve('/snippets/new/')
#         self.assertEqual(snippet_new, found.func)
class CreateSnippetsTest(TestCase):
    def serUp(self):
        self.user = UserModel.objects.create(
            username='test_user',
            email='test@example.com',
            password='top_secret_pass0001',
        )
        self.client.force_login(self.user)  # ログインする

    def test_render_create_form(self):
        response = self.client.get('/snippets/new/')
        self.assertContains(response, 'スニペットの登録', status_code=200)

    def test_create_snippet(self):
        data = {
            'title': 'タイトル',
            'code': 'コード',
            'description': '解説'
        }
        self.client.post('/snippets/new/', data)
        snippet = Snippet.objects.get(title='タイトル')
        self.assertEqual('コード', snippet.code)
        self.assertEqual('解説', snippet.description)


# class SnippetsDetailTest(TestCase):
#     def test_should_resolve_snippet_detail(self):
#         found = resolve('/snippets/1/')
#         self.assertEqual(snippet_detail, found.func)

class SnippetsDetailTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username='test_user',
            email='test@example.com',
            password='detail_secret_pass0001',
        )
        self.snippet = Snippet.objects.create(
            title='タイトル',
            code='コード',
            description='解説',
            create_by=self.user,
        )

    def test_should_use_expected_template(self):
        response = self.client.get('/snippets/%s/' % self.snippet.id)
        self.assertTemplateUsed(response, 'snippets/snippet_detail.html')

    def test_top_page_returns_200_and_expected_heading(self):
        response = self.client.get('/snippets/%s/' % self.snippet.id)
        self.assertContains(response, self.snippet.title, status_code=200)


class EditSnippetsTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve('/snippets/1/edit/')
        self.assertEqual(snippet_edit, found.func)
