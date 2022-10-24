from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse

from storyer.models import Student, Assignment
from django.contrib.auth.models import User

'''
return HttpResponse("Hello world. This is the Storyer project index")
'''


def index(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'initial.html')


def login(request):

    return render(request, 'login.html')


def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'student_detail.html', {'student': student})


def pick_groups(request, student_id):
    assignment_list = Assignment.objects.order_by('title')
    student = get_object_or_404(Student, pk=student_id)
    context = {
        'student': student,
        'group_list': assignment_list,
    }
    return render(request, 'index.html', context)
