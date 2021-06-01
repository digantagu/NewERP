# Generated by Django 3.2 on 2021-05-31 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('did', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=122)),
                ('img', models.CharField(max_length=122)),
                ('birthdoc', models.CharField(max_length=122)),
                ('castedoc', models.CharField(max_length=122)),
                ('marksheetdoc', models.CharField(max_length=122)),
            ],
        ),
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
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('eid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=122)),
                ('subject', models.CharField(max_length=122)),
                ('ses', models.CharField(max_length=122)),
                ('exam_id', models.CharField(max_length=122)),
                ('type', models.CharField(max_length=122)),
            ],
        ),
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
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=122)),
                ('nationality', models.CharField(max_length=100)),
                ('mtongue', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('caste', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=122)),
                ('dob', models.DateField()),
                ('school', models.CharField(max_length=122)),
                ('sad', models.CharField(max_length=122)),
                ('qua', models.CharField(max_length=122)),
                ('father', models.CharField(max_length=122)),
                ('fmail', models.EmailField(max_length=122)),
                ('phn', models.CharField(max_length=122)),
                ('job', models.CharField(max_length=122)),
                ('mother', models.CharField(max_length=122)),
                ('mailid', models.EmailField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('occ', models.CharField(max_length=100)),
                ('house', models.CharField(max_length=100)),
                ('vill', models.CharField(max_length=100)),
                ('postoffice', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]