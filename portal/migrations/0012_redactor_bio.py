# Generated by Django 4.1.4 on 2022-12-25 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0011_comments"),
    ]

    operations = [
        migrations.AddField(
            model_name="redactor",
            name="bio",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
