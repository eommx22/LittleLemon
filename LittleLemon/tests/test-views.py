from django.test import TestCase
from Restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="Tojásleves", price="8.50", inventory=8)
        Menu.objects.create(title="Málnatorta", price="12.50", inventory=6)
        Menu.objects.create(title="Almaleves", price="10", inventory=10)
        Menu.objects.create(title="Bableves", price="11.8", inventory=4)
        
     