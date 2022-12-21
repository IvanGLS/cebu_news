from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Redactor(AbstractUser):
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


class News(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=30000)
    location = models.CharField(max_length=20, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    publishers = models.ManyToManyField(Redactor,
                                        related_name="news",
                                        )
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 )
    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="featured_image/%Y/%m/%d/")

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return "{}".format(self.title)
