# Generated by Django 3.2.9 on 2021-11-16 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
