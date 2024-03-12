from django.shortcuts import render
from django.views.generic import View
from empapp.models import EmpMaster
# Create your views here.

def welcome(request):
    return render(request,'homepage.html')
class EmpInsertRec(View):
    def get(self,request):
        if(request.session.has_key('password')):
            request.session.set_expiry(60)
            return render(request,'insertEmpform.html')
        else:
            request.session['path']=request.path
            request.session.set_expiry(60)
            return render(request,'login.html')

    def post(self,request):
        id= request.POST['eid']
        name= request.POST['empname']
        sal= request.POST['salary']
        age= request.POST['age']
        dptno= request.POST['deptno']

        emp=EmpMaster(eid=id,ename=name,salary=sal,age=age,deptno=dptno)
        emp.save()
        return render(request, 'EmpStatus.html')

class ShowEmpRecs(View):
    def get(self,request):
        if (request.session.has_key('password')):
            recs = EmpMaster.objects.all()
            return render(request,'ShowEmpRecs.html',{'emprecs':recs})
        else:
            request.session['path']=request.path
            request.session.set_expiry(60)
            return render(request,'login.html')

class SearchEmp(View):
    def get(self,request):
        return render(request,'EmpSerach.html')
    def post(self,request):
        id=request.POST['eid']
        rec=EmpMaster.objects.get(eid=id)
        return render(request,'UpdateEmp.html',{'emprecs':rec})

class UpdateEmp(View):
    def get(self,request):
        if(request.session.has_key('password')):
            return render(request,'EmpSerach.html')
        else:
            request.session['path']=request.path
            request.session.set_expiry(60)
            return render(request,'login.html')

    def post(self,request):
        try:
            id=request.POST['eid']
            rec=EmpMaster.objects.get(eid=id)
            rec.ename = request.POST['empname']
            rec.salary = request.POST['salary']
            rec.age = request.POST['age']
            rec.deptno = request.POST['deptno']
            rec.save()
            recs=EmpMaster.objects.all()
            return render(request,'ShowEmpRecs.html',{'emprecs':recs,"msg":"Record Updated Successfully..."})
        except EmpMaster.DoesNotExist:
            return render(request, 'UpdateEmp.html', {"msg": "Invalid EmpId please try again..."})


class DeleteEmpRec(View):
    def get(self,request):
        return render(request,'DeleteEmp.html')
    def post(self,request):
        try:
            id=request.POST['eid']
            rec = EmpMaster.objects.get(eid=id)
            rec.delete()
            recs=EmpMaster.objects.all()
            return render(request,'ShowEmpRecs.html',{"emprecs":recs,"msg":"Record is deleted successfully..."})
        except EmpMaster.DoesNotExist:
            return render(request,'DeleteEmp.html',{"msg":"Invalid EmpId please try again..."})

def Logout(request):
    try:
        del request.session['mailid']
        del request.session['password']
        msg = 'Logged Out Successfully'
        return render(request,'homepage.html',{'msg':msg})
    except KeyError:
        return render(request,'homepage.html',{'msg':'Please Login first '})
