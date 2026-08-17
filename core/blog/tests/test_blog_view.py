from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

from blog.models import Post, Category

User = get_user_model()


class TestListPostView(TestCase):
    """
    Test the Post detail view.
    """

    def setUp(self):
        """
        This method runs before each test.
        """

        self.user = User.objects.create_user(
            email="test@gmail.com",
            password="testpassword",
        )

        self.profile = self.user.profile
        self.profile.first_name = "ali"
        self.profile.last_name = "karimi"
        self.profile.description = "for the test"
        self.profile.save()

        self.category = Category.objects.create(
            name="test"
        )

        self.post = Post.objects.create(
            author=self.profile,
            category=self.category,
            title="test",
            content="test post",
            published_date=timezone.now(),
        )

    def test_blog_post_detail(self):
        """
        Test that the Post detail page returns a successful response.
        """

        url = reverse(
            "blog:single_post",
            kwargs={"id": self.post.id},
        )
        
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)