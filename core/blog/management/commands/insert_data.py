from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from django.utils import timezone
import random

from accounts.models import Profile
from blog.models import Post, Category


User = get_user_model()


category_list = [
    "IT",
    "Backend",
    "frontend",
    "Programer",
    "developer",
]


class Command(BaseCommand):
    help = "Insert fake data for posts"

    def __init__(self, stdout=None, stderr=None, no_color=None, force_color=None):
        super().__init__(stdout, stderr, no_color, force_color)
        self.fake = Faker()

    def handle(self, *args, **options):

        email = self.fake.unique.email()

        user = User.objects.create_user(
            email=email,
            password="@1234567",
        )

        profile = Profile.objects.get(user=user)

        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=5)
        profile.save()
        
        for name in category_list:
            Category.objects.get_or_create(name=name)

        for _ in range(10):

            post = Post.objects.create(
                author=profile,
                title=self.fake.paragraph(nb_sentences=1),
                image="blog/default.jpg",
                content=self.fake.paragraph(nb_sentences=10),
                status=random.choice([True, False]),
                category=Category.objects.get(
                    name=random.choice(category_list)
                ),
                published_date=timezone.now(),
            )

        self.stdout.write(
            self.style.SUCCESS("Fake data created successfully!")
        )