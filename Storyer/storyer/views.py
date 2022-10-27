from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.http import HttpResponse

from storyer.models import Student, Assignment
from django.contrib.auth.models import User
from .forms import LoginForm, SignupForm


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        context = {}
        post_data = request.POST or None
        if post_data is not None:
            signup_form = SignupForm(post_data)
            if signup_form.is_valid():
                signup_form = signup_form.cleaned_data
                if not Student.objects.filter(email=signup_form['email']).exists():
                    name = (signup_form['first_name'].replace(" ", "").title(
                    ))+" "+signup_form['last_name'].replace(" ", "").title()
                    new_student = Student(
                        name=name, email=signup_form['email'], password=signup_form['password'])
                    new_student.save()
                    return student_detail(request, new_student.id)
                else:
                    context.update({"exists": True})
        context.update({'error_message': True})
        return render(request, 'initial.html', context)

    return render(request, 'initial.html')


# student login only
def login(request):
    if request.method == "POST":
        post_data = request.POST or None
        if post_data is not None:
            login_form = LoginForm(post_data)
            if login_form.is_valid():
                login_form = login_form.cleaned_data
                student = Student.objects.filter(
                    email=login_form['email'], password=login_form['password']).first()
                if student is not None:
                    return student_detail(request, student.id)
        context = {'error_message': True}
        return render(request, 'login.html', context)

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
    return render(request, 'pick_groups.html', context)
