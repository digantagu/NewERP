# Generated by Django 4.1.4 on 2022-12-20 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='mail',
        ),
        migrations.AddField(
            model_name='student',
            name='aadhaar',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='docs',
            name='marksheetdoc',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
    ]
