# Generated by Django 3.1.7 on 2021-02-23 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='mmail',
        ),
    ]