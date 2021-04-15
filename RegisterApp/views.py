from PIL.Image import Image
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from.forms import SignupUser,UserLoginForm
from django.contrib.auth.models import User
from RegisterApp.models import *
from  django.contrib.auth.decorators import login_required
#importing  forms class by above commamd


#creating for loging_view  for
def login_view(request):
    if request.method == 'POST' :
        form=SignupUser(request.  POST or None) # values for sign up form
        if form.is_valid(): # i will check this value valid or not
            form.save()
            return redirect(success)
    else:
        form = SignupUser()
    return render(request,'Signup.html',{'form':form})

def success(request):
    return render(request,'message.html')



#I am using userlogin create page
# created user login function
def UserLogin(request):
    if request.method == 'POST':
        loginform=UserLoginForm(request.POST or None)
        if loginform.is_valid(): # its checking login form valid or not
            username = loginform.cleaned_data.get('username')
            password = loginform.cleaned_data.get('password')
            user=authenticate(username=username,password=password)# this user/pass are valieds or not
            if user.is_active:
                login(request,user)
                return redirect(show_home_page)

    else:
        loginform = UserLoginForm()
    return render(request,'login.html',{'loginform':loginform})

"""def HomePage(request):
    return render(request,'Home.html')"""

def Profile(request,pk=None):
    if pk:
        user=User.objects.get(pk=pk)
    else:
        user=request.user
    return render(request,'profile.html',{'user':user})
def UserLogout(request):
    logout(request)
    return  redirect(UserLogin)



 #createing models view with images
def show_home_page(request):
    cats=Category.objects.all()
    images=Image.objects.all()
    data={'images':images ,'cats':cats}


    return render(request,'show.html',data)

#creating categeory page
def show_category_page(request,cid):
    cats=Category.objects.all()
    category=Category.objects.get(pk=cid)
    images=Image.objects.filter(cat=category)
    data={'images':images ,'cats':cats}


    return render(request,'show.html',data)

def signup(request):
    return redirect('/signup')







# Create your views here.
