from django.test import TestCase


# Create your tests here.
class LoginPageTest(TestCase):
    def test_login_page_returns_200(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_expected_template(self):
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'accounts/login.html')


class SignupPageTest(TestCase):
    def test_signup_page_returns_200(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_page_expected_template(self):
        response = self.client.get('/accounts/signup/')
        self.assertTemplateUsed(response, 'accounts/signup.html')
