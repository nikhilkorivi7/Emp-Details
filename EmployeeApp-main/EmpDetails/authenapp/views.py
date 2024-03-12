from django.shortcuts import render
from django.views.generic import View
from authenapp.models import user
# Create your views here.
def regPage(request):
    return render(request,'registration.html')
class RegisterUser(View):
    def get(self,request):
        return render(request, 'registration.html')
    def post(self,request):
        fname=request.POST['fstname']
        lname = request.POST['lstname']
        uname = request.POST['usrname']
        password = request.POST['pswd']
        mailid = request.POST['mailid']
        phone = request.POST['phone']
        user.objects.create(fname=fname,lname=lname,uname=uname,password=password,mailid=mailid,phone=phone)
        return render(request,'login.html')
class ChkLogin(View):
    def get(self,request):
        request.session['path']=''
        return render(request,'login.html')
        # if(request.session.has_key('password')):
        #     return render(request, 'homepage.html')
        # else:
        #     return render(request,'login.html')
    def post(self,request):
        password = request.POST['pswd']
        mailid = request.POST['mailid']
        rec=user.objects.filter(password=password,mailid=mailid)
        if(rec.count()):
            request.session['mailid']=mailid
            request.session['password']=password
            request.session.set_expiry(60)
            if(request.session['path']=='/empinsert/'):
                 return render(request,'insertEmpform.html')
            elif(request.session['path']=='/updateemp/'):
                 return render(request,'UpdateEmp.html')
            elif(request.session['path']=='/deleteemp/'):
                 return render(request,'DeleteEmp.html')
            elif(request.session['path']=='/showemp/'):
                 return render(request,'ShowEmpRecs.html')
            elif(request.session['path']=='/chklogin/'):
                 return render(request,'login.html')
            else:
                msg = "Login is successful"
                return render(request,'homepage.html',{"msg":msg})
        else:
            msg = 'Invalid Credentials ...Please try again'
            return render(request,'login.html',{'msg':msg})
