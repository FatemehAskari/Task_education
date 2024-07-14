from django.forms import ModelForm
from django.test import TestCase

from shop.forms import PersonalInformation


class TestHotSeatForm(TestCase):
    def setUp(self):
        self.form_data = {
            'gender': 'm',
            'full_name': 'Mohammad',
            'age': 38,
            'height': 210,
            'email': 'mymail@quera.com',
            'phone': '10121212',
            'mobile': '0021212'
        }
        self.valid_form = PersonalInformation(data=self.form_data)

    def test_form_base_class(self):
        answer = PersonalInformation.__base__
        expected_base_class = ModelForm
        self.assertEqual(answer, expected_base_class, msg='\nکلاس PersonalInformation باید از ModelForm ارث‌بری کرده‌ باشد.')