from django.test import TestCase
from Restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        item1=Menu.objects.create(title="Tojásleves", price="8.50", inventory=8)
        item2=Menu.objects.create(title="Málnatorta", price="12.50", inventory=6)
        item3=Menu.objects.create(title="Almaleves", price="10", inventory=10)
        item4=Menu.objects.create(title="Bableves", price="11.8", inventory=4)
        
        def test_getall():
            item1.assertEqual(item1, "Tojásleves : 8.50")
            item2.assertEqual(item2, "Málnatorta : 12.50")
            item3.assertEqual(item3, "Almaleves : 10")
            item4.assertEqual(item4, "Bableves : 11.8")