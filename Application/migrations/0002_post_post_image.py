# Generated by Django 4.0.3 on 2022-03-07 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(null=True, upload_to='post/image'),
        ),
    ]
