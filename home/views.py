from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
#create your view here
def index(request):
    return render(request,'page/home.html')

def contact(request):
    return render(request,'page/contact.html')

def error(request):
    return render(request,'page/error.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render (request,'page/register.html',{'form':form})
# Create your views here.
