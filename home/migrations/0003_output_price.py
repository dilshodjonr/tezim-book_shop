# Generated by Django 5.1.3 on 2025-01-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_book_model_category_alter_book_model_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='output',
            name='price',
            field=models.FloatField(default=0, verbose_name='Chiqim narxi'),
            preserve_default=False,
        ),
    ]
