import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import Permission
from blog.models import Category

User = get_user_model()


@pytest.fixture
def common_user():
    user = User.objects.create_user(email="test@gmail.com", password="@1234567")
    return user

@pytest.fixture
def user_permission(common_user):
    permission = Permission.objects.get(
        codename="add_post",
        content_type__app_label="blog",
    )

    create_user = common_user.user_permissions.add(permission)

    return create_user


@pytest.fixture
def profile(common_user):
    common_user.profile = common_user.profile
    common_user.profile.first_name = "ali"
    common_user.profile.last_name = "karimi"
    common_user.profile.description = "for the test"
    common_user.profile.save()

    return common_user.profile

@pytest.fixture
def category():
    category = Category.objects.create(
        name="test"
    )

    return category
            
@pytest.mark.django_db
class TestPostApi():
    client = APIClient()

    def test_get_post_api_response_status_200(self, common_user):
        user = common_user
        self.client.force_authenticate(user=user)
        url = reverse("blog:api-v1:post-list",)
        response = self.client.get(url)

        assert response.status_code == 200

    def test_create_post_response_status_401(self, category, profile):
        url = reverse("blog:api-v1:post-list")

        data = {
            "category": category.id,
            "title": "test",
            "content": "test post",
            "status":True,
            "published_date": timezone.now().date(),
        }

        response = self.client.post(url, data)

        assert response.status_code == 201

    def test_create_post_response_status_201(self, category, profile):
        url = reverse("blog:api-v1:post-list")

        data = {
            "author": profile.id,
            "category": category.id,
            "title": "test",
            "content": "test post",
            "status":True,
            "published_date": timezone.now().date(),
        }

        response = self.client.post(url, data)

        assert response.status_code == 201

    def test_create_post_invalid_data_response_status_400(self, category, profile):
        url = reverse("blog:api-v1:post-list")

        data = {
            "title": "test",
            "content": "test post",
            "status":True,
            "published_date": timezone.now().date(),
        }

        response = self.client.post(url, data)

        assert response.status_code == 400