# Generated by Django 4.2.5 on 2024-05-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_alter_article_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog.category', verbose_name='دسته بندی'),
        ),
    ]