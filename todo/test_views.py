from django.test import TestCase
from .models import Items
from django.shortcuts import get_object_or_404

class TestViews(TestCase):
    
    def test_get_home_page(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'todo_list.html')
        
    def test_gett_add_item_page(self):
        page = self.client.get('/add')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'item_form.html')
        
    def test_gett_edit_item_page(self):
        
        item = Items(name='Create a Test')
        item.save()
        
        page = self.client.get('/edit/{0}'.format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'item_form.html')
        
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get('/edit/1')
        self.assertEqual(page.status_code, 404)
        
    def test_post_create_an_item(self):
        response = self.client.post('/add', {'name': 'Create a test'})
        item = get_object_or_404(Items, pk=1)
        self.assertEqual(item.done, False)
    
    def test_post_edit_an_item(self):
        item = Items(name='Create a test')
        item.save()
        id = item.id
        
        response = self.client.post('/edit/{0}'.format(id), {'name': 'A different name'})
        item = get_object_or_404(Items, pk=id)
        
        self.assertEqual('A different name', item.name)
        
    def test_toggle_status(self):
        item = Items(name='Create a test')
        item.save()
        id = item.id
        
        response = self.client.post('/toggle/{0}'.format(id))
        item = get_object_or_404(Items, pk=id)
        self.assertEqual(item.done, True)