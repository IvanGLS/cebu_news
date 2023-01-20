from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Redactor(AbstractUser):
    image = models.ImageField(upload_to="media/%Y/%m/%d/", null=True)
    bio = models.CharField(max_length=255, null=True)
    years_of_experience = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(40),
            MinValueValidator(1)
        ]
     )

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Category(models.Model):
    category = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.category


class News(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=30000)
    location = models.CharField(max_length=20, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    most_popular = models.BooleanField(default=False)
    publishers = models.ForeignKey(Redactor,
                                   on_delete=models.CASCADE,
                                   related_name="news")
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 )
    image = models.ImageField(upload_to="media/%Y/%m/%d/")

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return "{}".format(self.title)


class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,)
    post = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name="comments", )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return "{}".format(self.content)
