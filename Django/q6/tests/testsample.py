from django.db.models import Sum
from django.test import TestCase

from askme import queries
from askme.models import Mobile


class TestTasks(TestCase):
    fixtures = ('store',)

    def test_total_value_of_products(self):
        solution = Mobile.objects.aggregate(total_value=Sum('price'))
        answer = queries.total_value_of_products()
        self.assertDictEqual(solution, answer, '\nتابع total_value_of_products باید با استفاده از تابع Sum، جمع ارزش تمامی موبایل‌های فروشگاه را بازگرداند.')