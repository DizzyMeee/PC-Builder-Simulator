# Generated by Django 3.2.9 on 2021-12-25 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komponen',
            name='nama_komponen',
            field=models.TextField(default='', max_length=255),
        ),
    ]