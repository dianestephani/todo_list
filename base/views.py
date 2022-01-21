from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 5. Creating simple view for testing. Then we'll add this view to our URL patterns.

def taskList(request):
    return HttpResponse('To Do List tester')