# Generated by Django 3.0.6 on 2021-01-22 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_api', '0005_auto_20210122_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam', models.IntegerField(primary_key=True, serialize=False)),
                ('section1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section1', to='quiz_api.Quiz')),
                ('section2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section2', to='quiz_api.Quiz')),
                ('section3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section3', to='quiz_api.Quiz')),
            ],
        ),
    ]
