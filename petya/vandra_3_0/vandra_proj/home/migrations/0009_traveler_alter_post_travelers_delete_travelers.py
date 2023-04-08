# Generated by Django 4.1.7 on 2023-04-03 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_post_travelers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='travelers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.traveler'),
        ),
        migrations.DeleteModel(
            name='Travelers',
        ),
    ]
