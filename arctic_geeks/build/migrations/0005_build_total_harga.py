# Generated by Django 3.2.9 on 2021-12-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0004_auto_20211216_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='total_harga',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
