# Generated by Django 4.0.1 on 2022-02-22 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_autor_delete_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='imagen',
            field=models.URLField(default='https://google.com'),
            preserve_default=False,
        ),
    ]
