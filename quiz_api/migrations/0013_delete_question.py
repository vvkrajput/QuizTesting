# Generated by Django 3.0.6 on 2021-01-24 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_api', '0012_delete_answer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]