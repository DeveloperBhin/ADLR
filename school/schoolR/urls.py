
from django.urls import path
from . import views

urlpatterns = [
     
    
    
    path('',views.User,name="User"),
    path('index/',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('userreg/',views.userreg,name="userregg"),
    path('schools/',views.schools,name="schools"),
    path('registration/',views.registration,name="registration"),
    path('NextOfKin1/',views.NextOfKin1,name="NextOfKin1"),
    path('NextOfKin2/',views.NextOfKin2,name="NextOfKin2"),
    path('NextOfKin3/',views.NextOfKin3,name="NextOfKin3"),
    path('education/',views.education,name="education"),
    path('applicantinfo/',views.applicantinfo,name="applicantinfo"),
    path('userinfo/',views.userinfo,name="userinfo"),
    path('result/',views.result,name="result"),
    path('selection/',views.selection,name="selection"),
    path('aboutus/',views.aboutus,name="aboutus"),
    
    
]
