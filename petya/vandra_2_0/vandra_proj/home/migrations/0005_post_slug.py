# Generated by Django 4.1.7 on 2023-04-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_post_options_post_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='nonslug'),
        ),
    ]