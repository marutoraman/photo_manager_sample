from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from university_photo.models import Picture
from .forms import ProductForm
from . import forms
from .exif import get_exif_info
from .models import MenuMaster

# Create your views here.
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request,'signup.html',{'success':'ユーザー登録できました。'})
        except IntegrityError:
            return render(request,'signup.html',{'error':'このユーザーは既に登録されています。'})
    return render(request,'signup.html')

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            return render(request,'login.html',{'error':'ログインできてません。'})
    return render(request,'login.html')

def menufunc(request):
    return render(request,'menu.html')

def form(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST,request.FILES)
        if form.is_valid():
            picture = form.cleaned_data['picture']
            get_info = get_exif_info(picture)
            print(get_info[0]) #曜日の表示
            print(get_info[1]) #時間の表示
            form.save()
            return redirect('login') 
    else:
        form = forms.ProductForm()
    return render(request,'picture.html',context={'form':form})

# class Picturefunc(CreateView):
#     template_name = 'picture.html'
#     model = Picture
#     fields = ('picture','description')
#     success_url = reverse_lazy('login')





   


