# Generated by Django 3.1.7 on 2021-02-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210223_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('enroll', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('ses', models.CharField(max_length=122)),
                ('cname', models.CharField(max_length=122)),
                ('section', models.CharField(max_length=122)),
                ('name', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]
