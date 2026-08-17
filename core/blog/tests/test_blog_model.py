from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from blog.models import Post, Category


User = get_user_model()


class TestBlogModel(TestCase):
    """
    Test the Post model.
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

    def test_blog_model_valid(self):
        """
        Test creating a Post successfully.
        """

        post = Post.objects.create(
            author=self.profile,
            category=self.category,
            title="test",
            content="test post",
            published_date=timezone.now(),
        )

        self.assertIsNotNone(post)

        self.assertEqual(post.title, "test")
        self.assertEqual(post.content, "test post")
        self.assertEqual(post.author, self.profile)
        self.assertEqual(post.category, self.category)