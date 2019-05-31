from django.test import TestCase
from .models import Items

class TestItemModel(TestCase):
    
    def test_dont_defaults_to_false(self):
        item = Items(name='Create a test')
        item.save()
        self.assertEqual(item.name, 'Create a test')
        self.assertFalse(item.done)
        
    def test_can_create_an_item_with_a_name_and_status(self):
        item = Items(name='Create a test', done=True)
        item.save()
        self.assertEqual(item.name, 'Create a test')
        self.assertTrue(item.done)
        
    def test_item_as_a_string(self):
        item = Items(name='Create a test')
        self.assertEqual('Create a test', str(item))