# Generated by Django 3.0.6 on 2021-01-24 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_api', '0011_delete_usersanswer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
