from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request, 'my_to_do_app/index.html')
    #return HttpResponse("my_to_do_app first page")

def createTodo(request):
    user_input_str = request.POST['todoContent']
    return HttpResponse("Create to do " + user_input_str)
