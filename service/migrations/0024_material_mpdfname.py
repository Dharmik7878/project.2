# Generated by Django 5.1.4 on 2025-02-01 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0023_remove_material_pdf_remove_material_sub1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='mpdfname',
            field=models.CharField(default=10, max_length=50),
            preserve_default=False,
        ),
    ]
