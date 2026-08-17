from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import Permission

User = get_user_model()

class TestBlogForm(TestCase):
    """
    Test creating a Post by a user with the required permission.
    """
        
    def setUp(self):
        """
        This method runs before each test.
        """
                
        self.user = User.objects.create_user(
            email="test@gmail.com",
            password="testpassword",
        )
        permission = Permission.objects.get(
            codename="add_post",
            content_type__app_label="blog",
        )

        self.user.user_permissions.add(permission)

        logged_in = self.client.login(
            email="test@gmail.com",
            password="testpassword",
        )
        self.assertTrue(logged_in)

    def test_blog_forms_valid(self):
        """
        Test submitting the Post creation form successfully.
        """
                
        response = self.client.post(
            reverse("blog:create_post"),
            {
                "title": "test",
                "content": "test post",
                "published_date": timezone.now(),
            }
        )

        self.assertEqual(response.status_code, 200)