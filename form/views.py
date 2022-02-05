from django.shortcuts import render

from django.shortcuts import render, redirect, HttpResponse
from .forms import StudentForm, UserCreateForm
from .models import StudentData
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def main(request):

    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('شكرا يا مسّاح')
        else:
            return HttpResponse('البيان دي ما اترفعت راجعهه منها تاني و اتاكد من الاندكس')
    
    context = {'form': form}
    return render(request, 'main.html', context)


def registerPage(request):
    form = UserCreateForm()
    context = {'form': form}

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('this is invalid form')
        else:
            return HttpResponse('invalid form')
            
    return render(request, 'register.html', context)


def loginForm(request):
    user = User.objects.all()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect('filterdata')
        else:
            return HttpResponse('هههههههههههه')
    
    # authenticate(username= username, password= password)
    
    context = {}
    return render(request, 'login.html', context)


def logOut(request):
    logout(request)
    return redirect('main')

@login_required(login_url='main')
def filterData(request):

    return render(request, 'filterdata.html')

@login_required(login_url='main')
def showData(requst, pk):
    data = StudentData.objects.filter(batch= pk)
    context = {'data': data}
    return render(requst, 'data.html', context)
