# Generated by Django 5.1.4 on 2025-01-23 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=30)),
                ('contact_Email', models.EmailField(max_length=40)),
                ('contact_subject', models.CharField(max_length=100)),
                ('contact_message', models.CharField(max_length=200)),
            ],
        ),
    ]
