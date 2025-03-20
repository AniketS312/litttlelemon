from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuItemTest(TestCase):
    def test_menu(self):
        item = Menu.objects.create(Title='Pizza', Price=10.00, Inventory=10)
        self.assertEqual(item, 'Pizza: 10.00')

class MenuViewTest(TestCase):
    def test_menu(self):
        self.item1 = Menu.objects.create(title="Pizza", price=10.00, inventory=10)
        self.item2 = Menu.objects.create(title="brushetta", price=8.50, inventory=20)
        self.item3 = Menu.objects.create(title="Pasta", price=12.00, inventory=15)
        
        items = Menu.objects.all()
        serialized_data = MenuSerializer(items, many=True).data

        expected_data = [
                {"id": self.item1.id, "title": "Pizza", "price": "10.00", "inventory": 10},
                {"id": self.item2.id, "title": "brushetta", "price": "8.50", "inventory": 20},
                {"id": self.item3.id, "title": "Pasta", "price": "12.00", "inventory": 15},
            ]
        self.assertEqual(serialized_data, expected_data)