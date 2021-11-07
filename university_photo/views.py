import datetime
from django.db.models.query import RawQuerySet
from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from university_photo.models import Picture
from .forms import ProductForm
from . import forms
from .exif import get_exif_info, get_file_created_at
from .models import MenuMaster, RegisterMenu

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
        picture_object = Picture()
        form = forms.ProductForm(request.POST, request.FILES, instance=picture_object)
        if form.is_valid():
            picture = form.cleaned_data['picture']
            try:
                #get_info = get_exif_info(picture)
                file_created_at = get_file_created_at(picture.read())
                created_time = datetime.time(file_created_at.hour, file_created_at.minute)
                print(created_time) 
                print(file_created_at.weekday()) 
                form.save()
            except Exception as e:
                print(e)
                form = forms.ProductForm()
            register_menu = RegisterMenu.objects.filter(user = request.user, 
                                                        menu__start_time__lte = created_time,
                                                        menu__finish_time__gte = created_time).first()
            print(register_menu)
            
            picture_object.register_menu = register_menu
            picture_object.save()
            #return redirect('login') 
    else:
        form = forms.ProductForm()
    return render(request,'picture.html',context={'form':form})

# class Picturefunc(CreateView):
#     template_name = 'picture.html'
#     model = Picture
#     fields = ('picture','description')
#     success_url = reverse_lazy('login')





   


