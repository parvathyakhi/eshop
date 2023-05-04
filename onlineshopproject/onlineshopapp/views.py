from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def demo(request):
    # return HttpResponse('My Own Online shopping app')
    return render(request,'index.html')