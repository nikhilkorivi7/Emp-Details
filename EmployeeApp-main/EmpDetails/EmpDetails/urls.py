"""EmpDetails URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authenapp.views import regPage,RegisterUser,ChkLogin
from empapp.views import EmpInsertRec,ShowEmpRecs,SearchEmp,UpdateEmp,DeleteEmpRec,welcome,Logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path("registration",regPage,name='reg'),
    path('registeruser',RegisterUser.as_view(),name='reguser'),
    path('chklogin',ChkLogin.as_view(),name='login'),
    path('empinsert',EmpInsertRec.as_view(),name="empins"),
    path('showemp',ShowEmpRecs.as_view(),name='showemp'),
    path('searchemp',SearchEmp.as_view(),name='searchemp'),
    path('updateemp',UpdateEmp.as_view(),name='upemp'),
    path('deleteemp',DeleteEmpRec.as_view(),name='delemp'),
    path('',welcome,name='home'),
    path('logout',Logout,name='logout')
]
