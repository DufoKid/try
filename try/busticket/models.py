from django.db import models

# Create your models here.
#define database
#huruf depan capitalise
#lepas tulis pergi terminal then run py manage.py makemigrations = involve db structure
#then run py manage.py migrate
#py manage.py shell
#from app.model import Class
#tulis dataprogramme=Class()
#then data.save()
#importprogramme1=Progamme.objects.get(programmecode='DLH')
#Progamme.objects.all().values() to display all values
#Subject.objects.filter(subjectcode='MPU2372').values() to display spesific data
#Subject.objects.filter(subjectcode='CSC2713').update(subjectcredithour=4)

class Programme(models.Model):
    programmecode= models.CharField(max_length=8,primary_key=True)
    programmename= models.TextField(max_length=50)
    programmeaccdate= models.DateField(null=True)
    programmeduration=models.IntegerField(default=3)

class Subject(models.Model):
    subjectcode= models.CharField(max_length=8,primary_key=True)
    subjectname= models.TextField(max_length=50)
    subjectcredithour= models.IntegerField(null=True)

class Mentor(models.Model):
    mentorid=models.CharField(max_length=11,primary_key=True)
    mentorname=models.TextField(max_length=70)
    mentor_student=models.TextField(max_length=50,null=True)

class Student(models.Model):
    studentid=models.CharField(max_length=11,primary_key=True)
    studentname=models.TextField(max_length=70)
    studenthobby=models.TextField(max_length=50,null=True)
    studentprogramme=models.ForeignKey(Programme,on_delete=models.CASCADE)
    studmentorid=models.ForeignKey(Mentor,on_delete=models.CASCADE,null=True, blank=True)
