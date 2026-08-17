from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import PostListView


class TestUrls(SimpleTestCase):

    def test_post_list_url(self):
        url = reverse("blog:list_post")
        view = resolve(url).func.view_class

        self.assertEqual(view, PostListView)