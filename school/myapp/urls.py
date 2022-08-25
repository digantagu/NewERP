from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.loginUser, name='login'),
                  path('logout', views.logoutUser, name='logout'),
                  path('signup', views.signup, name='signup'),
                  path('start', views.start, name='start'),
                  path('regstudent', views.regstudent, name='regstudent'),
                  path('regemployee', views.regemployee, name='regemployee'),
                  path('studentlist', views.studentlist, name='studentlist'),
                  path('enroll', views.enroll, name='enroll'),
                  path('studentdir', views.studentdir, name='studentdir'),
                  path('employeedir', views.employeedir, name='employeedir'),
                  path('guardiandir', views.guardiandir, name='guardiandir'),
                  path('examcreate', views.examcreate, name='examcreate'),
                  path('addmarks', views.addmarks, name='addmarks'),
                  path('viewsummary', views.viewsummary, name='viewsummary'),
                  path('savemarks', views.savemarks, name='savemarks'),
                  path('individualreport', views.individualreport, name='individualreport'),
                  path('reportcard', views.reportcard, name='reportcard'),
                  path('examwisereport', views.examwisereport, name='examwisereport'),
                  path('bulkadmission', views.bulkadmission, name='bulkadmission'),
                  path('employeelist', views.employeelist, name='employeelist'),
                  path('transferstudent', views.transferstudent, name='transferstudent'),
                  path('deactivate', views.deactivate, name='deactivate'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
