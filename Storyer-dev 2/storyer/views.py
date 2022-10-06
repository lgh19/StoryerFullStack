from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

'''
return HttpResponse("Hello world. This is the Storyer project index")
'''
def index(request):
    return render(request, 'index.html')