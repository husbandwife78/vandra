# Generated by Django 4.2 on 2023-04-15 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_alter_post_post_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_size",
            field=models.CharField(
                choices=[("Common", "1"), ("Big", "2")], default="Common", max_length=50
            ),
        ),
    ]
