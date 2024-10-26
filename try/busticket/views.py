from django.shortcuts import render, get_object_or_404
from busticket.models import Programme, Mentor, Student
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

def index(request):
    myprogramme = Programme.objects.all().values()
    mymentor = Mentor.objects.all().values()
    mystudent = Student.objects.all().values()
    context = {
        'nickname': 'Safini',
        'myprogramme': myprogramme,
        'mymentor': mymentor,
        'mystudent': mystudent
    }
    return render(request, "index.html", context)

def newmentor(request):
    mymentor = Mentor.objects.all().values()
    
    if request.method == 'POST':
        mentorid = request.POST['mentorid']
        mentorname = request.POST['mentorname']
        mentor_student = request.POST['mentor_student']
        
        data = Mentor(mentorid=mentorid, mentorname=mentorname, mentor_student=mentor_student)
        data.save()
        
        context = {
            'mymentor': mymentor,
            'message': 'NEW MENTOR HAS BEEN SAVED'
        }
        return render(request, "newmentor.html", context)
    else:
        context = {
            'mymentor': mymentor,
            'message': ''
        }
        return render(request, "newmentor.html", context)

def newstudent(request):
    myprogramme = Programme.objects.all().values()
    mymentor = Mentor.objects.all().values()
    mystudent = Student.objects.all().values()

    if request.method == 'POST':
        studentid = request.POST['studentid']
        studentname = request.POST['studentname']
        studenthobby = request.POST['studenthobby']
        studentprogramme = Programme.objects.get(pk=request.POST['studentprogramme'])
        studmentorid = Mentor.objects.get(pk=request.POST['studmentorid'])
        
        data = Student(studentid=studentid, studentname=studentname, studenthobby=studenthobby,
                       studentprogramme=studentprogramme, studmentorid=studmentorid)
        data.save()
        
        context = {
            'myprogramme': myprogramme,
            'mymentor': mymentor,
            'mystudent': mystudent,
            'message': 'NEW STUDENT HAS BEEN SAVED'
        }
        return render(request, "newstudent.html", context)
    else:
        context = {
            'myprogramme': myprogramme,
            'mymentor': mymentor,
            'mystudent': mystudent,
            'message': ''
        }
        return render(request, "newstudent.html", context)

def updatementor(request, mentor_id):
    mentor = Mentor.objects.get(mentorid=mentor_id)
    mymentor = Mentor.objects.all()  # Retrieve the list of all mentors
    
    context = {
        'mentor': mentor,  # Pass the mentor to update
        'mymentor': mymentor,  # Pass the list of all mentors
        'message': 'Page rendered, Data is not UPDATED yet'
    }
    return render(request, "updatementor.html", context)


def updatedatamentor(request, mentor_id):

    mentor=Mentor.objects.get(mentorid=mentor_id)
    mentor.mentorname = request.POST['mentorname']
    mentor.mentor_student = request.POST['mentor_student']
    mentor.save()
    
    return HttpResponseRedirect(reverse("newmentor")) 

def updatestudent(request, student_id):
    student = Student.objects.get(studentid=student_id)
    myprogramme = Programme.objects.all()
    mymentor = Mentor.objects.all()
    mystudent = Student.objects.all()  # Get all students for display

    context = {
        'student': student,
        'myprogramme': myprogramme,
        'mymentor': mymentor,
        'mystudent': mystudent,  # Pass student list to template
        'message': 'Page rendered, data is not UPDATED yet'
    }
    
    return render(request, "updatestudent.html", context)


def updatedatastudent(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(studentid=student_id)
        student.studentname = request.POST['studentname']
        student.studenthobby = request.POST['studenthobby']
        student.studentprogramme_id = request.POST['studentprogramme']
        student.studmentorid_id = request.POST['studmentorid']
        student.save()
        
        return HttpResponseRedirect(reverse("newstudent"))

def deletestud(request, student_id):
    student = Student.objects.get(studentid=student_id)
    myprogramme = Programme.objects.all()
    mymentor = Mentor.objects.all()
    mystudent = Student.objects.all()  # Get all students for display

    if request.method == 'POST':
        # Delete the student record
        student.delete()

        # Prepare context after deletion
        context = {
            'myprogramme': myprogramme,
            'mymentor': mymentor,
            'mystudent': mystudent,  # Pass student list to template
            'message': 'Student deleted successfully!'
        }
        return render(request, "student_list.html", context)  # Redirect to a list of students

    # If GET request, render the delete confirmation page with student data
    context = {
        'student': student,
        'myprogramme': myprogramme,
        'mymentor': mymentor,
        'mystudent': mystudent,  # Pass student list to template
        'message': 'Are you sure you want to delete this student?'
    }
    
    return render(request, "deletestud.html", context)  # Render delete confirmation template

def catalogue_ms(request):
    return render(request, "catalogue_ms.html")
