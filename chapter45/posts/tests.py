from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Post

# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(content='test')

    def test_content(self):
        myPost = Post.objects.get(id=1)
        myContent = f'{myPost.content}'
        print(myContent)
        self.assertEqual(myContent, 'test')

class HomePageTest(TestCase):
    def setUp(self):
        Post.objects.create(content="test")
    
    def test_home_page_status_by_address(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_home_page_status_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_home_page_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

