from django.contrib import admin

from .models import Student, Enroll, Examination, Savemarks, Docs, Attendance

admin.site.register(Student)
admin.site.register(Enroll)
admin.site.register(Examination)
admin.site.register(Savemarks)
admin.site.register(Docs)
admin.site.register(Attendance)
