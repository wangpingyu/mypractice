# Generated by Django 2.2.7 on 2019-12-10 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]
