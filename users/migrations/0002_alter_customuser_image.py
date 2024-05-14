# Generated by Django 5.0.6 on 2024-05-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="image",
            field=models.ImageField(
                blank=True,
                default="default_img/user_img.png",
                null=True,
                upload_to="users_images/",
            ),
        ),
    ]