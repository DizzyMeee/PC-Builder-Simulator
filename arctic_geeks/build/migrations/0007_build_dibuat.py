# Generated by Django 3.2.9 on 2021-12-18 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0006_build_build_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='dibuat',
            field=models.DateField(auto_now=True),
        ),
    ]
