# Generated by Django 5.1.4 on 2025-01-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_course_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timg', models.URLField(max_length=500)),
                ('tname', models.CharField(max_length=50)),
                ('tcourse', models.CharField(max_length=20)),
            ],
        ),
    ]
