# Generated by Django 4.2.5 on 2024-05-03 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publish'], 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
    ]
