# Generated by Django 3.0.6 on 2021-02-02 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_api', '0022_auto_20210127_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz_api.Quizer'),
        ),
    ]
