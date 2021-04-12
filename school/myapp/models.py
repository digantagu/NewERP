from django.db import models


class Student(models.Model):
    sid = models.AutoField(auto_created=True, serialize=False, primary_key=True)
    name = models.CharField(max_length=122)
    nationality = models.CharField(max_length=100)
    mtongue = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    caste = models.CharField(max_length=100)
    mail = models.EmailField(max_length=122)
    dob = models.DateField()
    school = models.CharField(max_length=122)
    sad = models.CharField(max_length=122)
    qua = models.CharField(max_length=122)
    father = models.CharField(max_length=122)
    fmail = models.EmailField(max_length=122)
    phn = models.CharField(max_length=122)
    job = models.CharField(max_length=122)
    mother = models.CharField(max_length=122)
    mailid = models.EmailField(max_length=122)
    phone = models.CharField(max_length=122)
    occ = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    vill = models.CharField(max_length=100)
    postoffice = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name


class Enroll(models.Model):
    objects = None
    enroll = models.AutoField(auto_created=True, serialize=False, primary_key=True)
    ses = models.CharField(max_length=122)
    cname = models.CharField(max_length=122)
    section = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name


class Examination(models.Model):
    objects = None
    eid = models.AutoField(auto_created=True, serialize=False, primary_key=True)
    cname = models.CharField(max_length=122)
    subject = models.CharField(max_length=122)
    ses = models.CharField(max_length=122)
    exam_id = models.CharField(max_length=122)
    type = models.CharField(max_length=122)

    def __str__(self):
        return self.exam_id


class Savemarks(models.Model):
    objects = None
    id = models.AutoField(auto_created=True, serialize=False, primary_key=True)
    rollnumber = models.CharField(max_length=122)
    enrollnumber = models.CharField(max_length=122)
    studentname = models.CharField(max_length=122)
    classname = models.CharField(max_length=122)
    sectionname = models.CharField(max_length=122)
    totalmarks = models.CharField(max_length=122)
    obtained = models.CharField(max_length=122)
    notebook = models.CharField(max_length=122)
    percentage = models.CharField(max_length=122)
    exam_id = models.CharField(max_length=122)
    sub = models.CharField(max_length=122)
    type = models.CharField(max_length=122)
    sub_en = models.CharField(max_length=122)
    ses = models.CharField(max_length=122)

    def __str__(self):
        return self.studentname
