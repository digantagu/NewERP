# Generated by Django 3.1.7 on 2021-03-03 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_examination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Savemarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('rollnumber', models.CharField(max_length=122)),
                ('enrollnumber', models.CharField(max_length=122)),
                ('studentname', models.CharField(max_length=122)),
                ('classname', models.CharField(max_length=122)),
                ('sectionname', models.CharField(max_length=122)),
                ('totalmarks', models.CharField(max_length=122)),
                ('obtained', models.CharField(max_length=122)),
                ('notebook', models.CharField(max_length=122)),
                ('percentage', models.CharField(max_length=122)),
                ('exam_id', models.CharField(max_length=122)),
                ('sub', models.CharField(max_length=122)),
                ('type', models.CharField(max_length=122)),
                ('sub_en', models.CharField(max_length=122)),
                ('ses', models.CharField(max_length=122)),
            ],
        ),
    ]