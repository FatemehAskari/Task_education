from django.test import TestCase, Client


class TestAll(TestCase):
    def setUp(self):
        self.client = Client()

    def test_1(self):
        response = self.client.get('/sad/yahya/')
        self.assertEqual(response.status_code, 200, '\nآدرس /sad/yahya/ یک url معتبر است؛ پس ریکوئست موفقیت‌آمیز خواهد بود.')

        content = response.content.decode('utf-8').strip()
        self.assertEqual('Nobody likes you, yahya!', content, '\nدر صورتی که به آدرس /sad/yahya/ ریکوئست زده شود؛ ریسپانس برابر Nobody likes you, yahya! خواهد بود.')