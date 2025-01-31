# Generated by Django 5.1.3 on 2024-11-22 10:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='refrences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='refrences nomi')),
                ('value', models.CharField(max_length=255, verbose_name='refrences qiymati')),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Chiqim malumoti')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Chiqim sanasi')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.refrences', verbose_name='Chiqim nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Sotilgan kitob soni')),
                ('price', models.FloatField(verbose_name='Sotilgan kitob narxi')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Sotilgan kitob sanasi')),
                ('sold_book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.refrences', verbose_name='Sotilgan kitob nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Xarajat narxi')),
                ('description', models.TextField(verbose_name='Xarajat malumoti')),
                ('quantity', models.IntegerField(verbose_name='Xarajat miqdori')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Xarajat sanasi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='costs_as_category', to='home.refrences', verbose_name='Xarajat turi')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='costs_as_name', to='home.refrences', verbose_name='Xarajat nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Book_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Kitob tavsifi')),
                ('price', models.FloatField(verbose_name='Kitob narxi')),
                ('quantity', models.IntegerField(verbose_name='Kitob soni')),
                ('image', models.ImageField(upload_to='media', verbose_name='Kitob rasmi')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Kitob qoshilgan sanasi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='books_as_category', to='home.refrences', verbose_name='Kitob turi')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='books_as_name', to='home.refrences', verbose_name='Kitob nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Xodimning tolig ismi')),
                ('phone_number', models.TextField(verbose_name='Xodimning telefon raqami')),
                ('birthday', models.DateField(verbose_name='Xodimning tugulgan sanasi')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.refrences', verbose_name='Xodimning jinsi')),
            ],
        ),
        migrations.CreateModel(
            name='Staff_Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Ishlagan xodimning maoshi')),
                ('time_work', models.FloatField(verbose_name='Ishlagan xodimning ish vaqti')),
                ('paid_price', models.FloatField(verbose_name='Ishlagan xodimga tolangan summa')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.staff', verbose_name='Ishlagan xodim')),
            ],
        ),
    ]
