from django.db import models

# Create your models here.
class EmpMaster(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100)
    salary = models.FloatField()
    age = models.IntegerField()
    deptno = models.IntegerField()
    def __str__(self):
        return '%d,%s,%f,%d,%d'%(self.eid,self.ename,self.salary,self.age,self.deptno)

