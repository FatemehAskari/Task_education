from datetime import date
from django.test import TestCase, Client

from library_management.models import Book


class TestAll(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_sample(self):
        Book.objects.create(author='Saeid', title="first", available=True)
        Book.objects.create(author='Mohammad', title="second", available=True)
        Book.objects.create(author='Ali', title="third", available=False)
        Book.objects.create(author='Sajjad', title="fourth", available=True)
        Book.objects.create(author='Farhad', title="fifth", available=False)

        response = self.cli.get('/booklist/')

        self.assertEqual(response.status_code, 200)

        self.assertTrue('Saeid wrote first.' in response.content.decode('utf-8'), '\nblock content را به درستی پیاده‌سازی نکرده‌اید.')
        self.assertTrue('Mohammad wrote second.' in response.content.decode('utf-8'), '\nblock content را به درستی پیاده‌سازی نکرده‌اید.')
        self.assertFalse('Ali wrote third.' in response.content.decode('utf-8'), '\nblock content را به درستی پیاده‌سازی نکرده‌اید.')
        self.assertFalse('Sajjad wrote second.' in response.content.decode('utf-8'), '\nblock content را به درستی پیاده‌سازی نکرده‌اید.')
        self.assertFalse('Farhad wrote fifth.' in response.content.decode('utf-8'), '\nblock content را به درستی پیاده‌سازی نکرده‌اید.')
        self.assertTrue('This page belongs to Quera.' in response.content.decode('utf-8'), '\nعبارت This page belongs to Quera. را به درستی نمایش نمی‌دهید.')
        self.assertTrue('Library' in response.content.decode('utf-8'), '\nعنوان (title) را باید برابر Library قرار دهید.')