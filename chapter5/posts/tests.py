from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):

        self.myUser = get_user_model().objects.create(
            username="test",
            email="",
            password="test"
        )

        self.myPost = Post.objects.create(
            title="my title",
            body="my body",
            author=self.myUser
        )

    def test_created_post(self):
        self.assertEqual(self.myPost.title, "my title")
        self.assertEqual(self.myPost.body, "my body")
        self.assertEqual(self.myPost.author, self.myUser)

    def test_post_list_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "my title")
        self.assertTemplateUsed(resp, 'home.html')
    
    def test_post_detail_view(self):
        resp = self.client.get('/detail/1')
        no_resp = self.client.get('/detail/188')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertContains(resp, "my title")
        self.assertTemplateUsed(resp, 'detail.html')
    
    
        