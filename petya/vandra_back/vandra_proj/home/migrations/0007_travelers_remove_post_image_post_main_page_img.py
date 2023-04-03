# Generated by Django 4.1.7 on 2023-04-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travelers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('avatar', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='main_page_img',
            field=models.ImageField(blank=True, null=True, upload_to='home/post_images/main_page_images'),
        ),
    ]