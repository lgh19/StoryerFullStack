from django.urls import path

from . import views

app_name = 'storyer'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('groups/<int:student_id>/', views.pick_groups, name='pick_groups'),
]
