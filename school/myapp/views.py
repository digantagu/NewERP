from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Student, Enroll, Examination, Savemarks
from tablib import Dataset
from .resources import BulkStudent
import xlrd
import os, sys
from django.core.files.storage import FileSystemStorage


def loginUser(request):
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        user = auth.authenticate(username=username1, password=password1)
        if user is not None:
            login(request, user)
            return render(request, 'start.html')
        else:
            messages.error(request, 'Username Or Password is incorrect')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('mid')
        psw = request.POST.get('psw')
        user = User.objects.create_user(username=name, email=email, password=psw)
        user.is_superuser = True
        user.is_staff = True
        user.save()
    return render(request, 'signup.html')


def logoutUser(request):
    logout(request)
    return redirect('/')


@login_required(login_url="/")
def start(request):
    return render(request, 'start.html')


@login_required(login_url="/")
def studentdir(request):
    return render(request, 'studentdir.html')


@login_required(login_url="/")
def employeedir(request):
    return render(request, 'employeedir.html')


@login_required(login_url="/")
def guardiandir(request):
    return render(request, 'guardiandir.html')


@login_required(login_url="/")
def examcreate(request):
    if request.method == "POST":
        cname = request.POST.get('cname')
        subject = dict(request.POST)['subject']
        ses = request.POST.get('ses')
        type = request.POST.get('type')

        for i in range(len(subject)):
            sub = subject.pop(0)
            mylist = [ses, type, cname, sub]
            s = '/'
            exam_id = s.join(mylist)

            exam1 = Examination(cname=cname, subject=subject, ses=ses, exam_id=exam_id, type=type)

            exam1.save()

        return redirect('/examcreate')

    return render(request, 'examcreate.html')


@login_required(login_url="/")
def regstudent(request):
    global name, student1
    if request.method == "POST":
        name = request.POST.get('fname')
        nationality = request.POST.get('nationality')
        mtongue = request.POST.get('mtongue')
        gender = request.POST.get('gender')
        caste = request.POST.get('caste')
        mail = request.POST.get('mail')
        dob = request.POST.get('dob')
        school = request.POST.get('school')
        sad = request.POST.get('sad')
        qua = request.POST.get('qua')
        father = request.POST.get('father')
        fmail = request.POST.get('fmail')
        phn = request.POST.get('phn')
        job = request.POST.get('job')
        mother = request.POST.get('mother')
        mailid = request.POST.get('momail')
        phone = request.POST.get('phone')
        occ = request.POST.get('occ')
        house = request.POST.get('hn')
        vill = request.POST.get('vill')
        postoffice = request.POST.get('po')
        district = request.POST.get('dist')
        state = request.POST.get('state')
        pin = request.POST.get('pin')

        '''
        img = request.FILES.get('img')
        birthdoc = request.FILES.get('bdoc')
        castedoc = request.FILES.get('cdoc')
        marksheetdoc = request.FILES.get('mdoc')

        fs = FileSystemStorage()
        fs.save(img.name, img)
        fs.save(birthdoc.name, birthdoc)
        fs.save(castedoc.name, castedoc)
        fs.save(marksheetdoc.name, marksheetdoc)

        img = fs.url(img)
        birthdoc = fs.url(birthdoc)
        castedoc = fs.url(castedoc)
        marksheetdoc = fs.url(marksheetdoc)

        doc1 = Docs(name=name, img=img, birthdoc=birthdoc, castedoc=castedoc, marksheetdoc=marksheetdoc)'''

        student1 = Student(name=name, nationality=nationality, mtongue=mtongue, gender=gender, caste=caste, mail=mail,
                           dob=dob, school=school, sad=sad, qua=qua, father=father, fmail=fmail, phn=phn, job=job,
                           mother=mother, mailid=mailid, phone=phone, occ=occ, house=house, vill=vill,
                           postoffice=postoffice, district=district, state=state, pin=pin,
                           date=datetime.today())

        return redirect('/enroll')

    return render(request, 'regstudent.html')


@login_required(login_url="/")
def enroll(request):
    if request.method == "POST":
        cname = request.POST.get('cname')
        section = request.POST.get('section')
        ses = request.POST.get('ses')

        enrolldata = Enroll(cname=cname, section=section, name=name, ses=ses, date=datetime.today())

        student1.save()
        enrolldata.save()
        return redirect('/regstudent')

    context = {}
    context['var'] = name
    return render(request, 'enroll.html', context)


@login_required(login_url="/")
def addmarks(request):
    global var1, v2
    results = Examination.objects.all()
    if request.method == "POST":
        myresult = Enroll.objects.all()
        exam_id = request.POST.get('ed')
        section = request.POST.get('sec')

        myvar = results.filter(exam_id=exam_id)

        for l in myvar:
            v1 = l.cname
            v2 = l.exam_id

            var1 = myresult.filter(cname=v1) & myresult.filter(section=section)

        for k in var1:
            cls = k.cname

        return render(request, 'putmarks.html', {"context": var1, 'exam_id': exam_id, 'section': section, 'cls': cls})

    return render(request, 'addmarks.html', {"Exam": results})


@login_required(login_url="/")
def viewsummary(request):
    global marks, total, per, note, roll, sub_en

    if request.method == "POST":
        total = dict(request.POST)['total']
        marks = dict(request.POST)['marks']
        note = dict(request.POST)['notebook']
        sub_en = dict(request.POST)['sub_en']

        roll = []
        cal = 1
        while int(cal) < len(var1) + 1:
            roll.append(cal)
            cal = int(cal) + 1

        for i in range(0, len(marks)):
            marks[i] = float(marks[i])

        per = [i * 0.2 for i in marks]
        note = [float(i) for i in note]
        sub_en = [float(i) for i in sub_en]

        mydict = {'var1': var1, 'marks': marks, 'roll': roll, 'per': per, 'note': note, 'total': total, 'vary': v2,
                  'sub_en': sub_en}

    return render(request, 'viewsummary.html', mydict)


@login_required(login_url="/")
def savemarks(request):
    if request.method == "POST":
        for record in var1:
            enrollnumber = record.enroll
            studentname = record.name
            classname = record.cname
            sectionname = record.section
            rollnumber = roll.pop(0)
            totalmarks = total.pop(0)
            obtained = marks.pop(0)
            percentage = per.pop(0)
            notebook = note.pop(0)
            suben = sub_en.pop(0)

            exam_id = v2

            var = exam_id.split('/')
            type = var[1]
            ses = var[0]
            sub = var[3]

            mydata = Savemarks(rollnumber=rollnumber, sub_en=suben, totalmarks=totalmarks, obtained=obtained,
                               percentage=percentage,
                               notebook=notebook,
                               exam_id=exam_id, enrollnumber=enrollnumber, studentname=studentname, classname=classname,
                               sectionname=sectionname, type=type, ses=ses, sub=sub)

            mydata.save()

    return redirect('/addmarks')


@login_required(login_url="/")
def individualreport(request):
    qry = Enroll.objects.all()
    if request.method == "POST":
        classname = request.POST.get('cname')
        sectionname = request.POST.get('sectionname')

        var2 = qry.filter(cname=classname) & qry.filter(section=sectionname)
        mylist = {'var2': var2}

        return render(request, 'filterreport.html', mylist)

    return render(request, 'individualreport.html')


@login_required(login_url="/")
def reportcard(request):
    sublist = []
    global type, ty, mylist
    if request.method == "POST":
        stname = request.POST.get('studentname')
        type = request.POST.get('type')
        ses = request.POST.get('ses')

        sname = Savemarks.objects.filter(studentname=stname) & Savemarks.objects.filter(
            type=type) | Savemarks.objects.filter(ses=ses)

        if type == 'PT I' or type == 'PT II':
            for i in sname:
                '''con = i.exam_id
                var = con.split('/')
                sublist.append(var[2])'''
                sublist.append(i.sub)

            total = []
            for num in sname:
                cone = num.obtained
                total.append(cone)

            mytotal = [float(i) for i in total]
            mysum = sum(mytotal)

            grade = []
            for i in sname:
                marks = float(i.obtained)

                if 45.5 <= marks <= 50:
                    grade.append('A1')
                elif 40.5 <= marks <= 45:
                    grade.append('A2')
                elif 35.5 <= marks <= 40:
                    grade.append('B1')
                elif 30.5 <= marks <= 35:
                    grade.append('B2')
                elif 25.5 <= marks <= 30:
                    grade.append('C1')
                elif 20.5 <= marks <= 25:
                    grade.append('C2')
                elif 16.5 <= marks <= 20:
                    grade.append('D')
                elif 0 <= marks <= 16:
                    grade.append('E')

            mylist = {'sname': sname, 'sublist': sublist, 'mysum': mysum, 'grade': grade}

            return render(request, 'ptreport.html', mylist)

        elif type == 'Term I' or type == 'Term II':

            if type == 'Term I':
                ty = 'PT I'
            elif type == 'Term II':
                ty = 'PT II'

            perlist = Savemarks.objects.filter(type=ty) & Savemarks.objects.filter(studentname=stname)

            li = []
            for l in perlist:
                li.append(l.percentage)

            print("elif is working....")

            for p in sname:
                print(p)

            for i in sname:
                sublist.append(i.sub)

            total = []
            for num in sname:
                cone = num.obtained
                total.append(cone)

            se = []
            for num in sname:
                cone = num.sub_en
                se.append(cone)

            note = []
            for num in sname:
                cone = num.notebook
                note.append(cone)

            test = []
            testy = []
            for j in sname:
                test.append(j.obtained)
                test.append(j.sub_en)
                test.append(j.notebook)
                q = li.pop(0)
                test.append(q)

                subtotal = [float(i) for i in test]

                subt = sum(subtotal)
                testy.append(subt)
                test.clear()

            mysum = sum(float(i) for i in testy)

            grade = []
            for m in testy:
                ma = float(m)
                if 90.5 <= ma <= 100:
                    grade.append('A1')
                elif 80.5 <= ma <= 90.5:
                    grade.append('A2')
                elif 70.5 <= ma <= 80.5:
                    grade.append('B1')
                elif 60.5 <= ma <= 70.5:
                    grade.append('B2')
                elif 50.5 <= ma <= 60.5:
                    grade.append('C1')
                elif 40.5 <= ma <= 50.5:
                    grade.append('C2')
                elif 32.5 <= ma <= 40.5:
                    grade.append('D')
                elif 0 <= ma <= 32.5:
                    grade.append('E')

            mylist = {'testy': testy, 'sname': sname, 'sublist': sublist, 'mysum': mysum, 'grade': grade,
                      'per': perlist}

    return render(request, 'reportcard.html', mylist)


@login_required(login_url="/")
def examwisereport(request):
    global sec
    secr = Savemarks.objects.all()
    input = Examination.objects.all()
    if request.method == "POST":
        eid = request.POST.get('exam_id')
        section = request.POST.get('sectionname')
        myv = secr.filter(exam_id=eid) & secr.filter(sectionname=section)
        if myv.exists():
            for s in myv:
                sec = s.sectionname
            return render(request, 'examwisemarks.html', {'secall': myv, 'type': type, 'eid': eid, 'sec': sec})
        else:
            return render(request, 'examwisereport.html', {'exam': input})

    return render(request, 'examwisereport.html', {'exam': input})


@login_required(login_url="/")
def bulkadmission(request):
    if request.method == "POST":
        cname = request.POST.get('cname')
        section = request.POST.get('section')
        adm = request.FILES.get('adm')

        fs = FileSystemStorage()
        fs.save(adm.name, adm)
        path = fs.url(adm)

        newpath = '/home/rtps/PycharmProjects/NewERP/school' + path
        print(newpath)

        wb = xlrd.open_workbook(newpath)
        sheet = wb.sheet_by_index(0)

        sheet.cell_value(0, 0)

        for i in range(sheet.nrows):
            print(sheet.row_values(i, 0))


        '''
        bulk_adm = BulkStudent()

        dataset = Dataset()

        adm = request.FILES.get('adm')
        
        fs = FileSystemStorage()
        fs.save(adm.name, adm)
        burl = fs.url(adm)
       

        print(adm)

        imported_data = dataset.load(adm.read())
        result = bulk_adm.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            bulk_adm.import_data(dataset, dry_run=False)  # Actually import now
            
            '''

    return render(request, 'bulkadmission.html')


@login_required(login_url="/")
def studentlist(request):
    return render(request, 'studentlist.html')
