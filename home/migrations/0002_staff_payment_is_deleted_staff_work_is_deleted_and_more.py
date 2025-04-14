# Generated by Django 5.1.3 on 2025-03-26 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_payment',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='O‘chirilganmi?'),
        ),
        migrations.AddField(
            model_name='staff_work',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='O‘chirilganmi?'),
        ),
        migrations.AlterField(
            model_name='staff_payment',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='To‘lov sanasi'),
        ),
        migrations.AlterField(
            model_name='staff_payment',
            name='price',
            field=models.FloatField(verbose_name='To‘langan summa'),
        ),
        migrations.AlterField(
            model_name='staff_payment',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.staff', verbose_name='Xodim'),
        ),
        migrations.AlterField(
            model_name='staff_work',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='To‘lov sanasi'),
        ),
    ]
