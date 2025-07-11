# Generated by Django 5.1.4 on 2025-01-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admname', models.CharField(max_length=70)),
                ('admEmail', models.EmailField(max_length=50)),
                ('admPhoneNumber', models.TextField(max_length=50)),
                ('admDateOfBirth', models.TextField(max_length=10)),
                ('admGender', models.CharField(max_length=10)),
                ('admaddress', models.TextField(max_length=150)),
                ('admcourse', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_message',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_subject',
            field=models.TextField(max_length=100),
        ),
    ]
