# Generated by Django 2.2.7 on 2019-12-10 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_id',
            field=models.IntegerField(default=None),
        ),
    ]
