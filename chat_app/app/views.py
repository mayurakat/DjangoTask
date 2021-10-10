from django.db.models.base import Model
from django.shortcuts import render,redirect
from .models import blogs
from django.contrib.auth.models import Permission, User, auth
from django.contrib import messages
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse




# Create your views here.
def home(request):

   
    return render(request,"home.html")





def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username = username).exists():

                messages.info(request, "username taken")
                return redirect('register')
                
            elif User.objects.filter(email = email).exists():

                messages.info(request,"email taken")
                return redirect('register')


            else:
                user = User.objects.create_user(username = username, email= email, password = password1, first_name = first_name , last_name = last_name )
                user.save();
                print("user Created")
                messages.info(request, "user Create")
                return redirect('login')

        else:

            messages.info(request,"password not match")
            return redirect('register')
            return redirect('home')


    else:
        return render(request, 'register.html')
        


def login(request):


    if request.method == 'POST':


        username = request.POST.get('email')
        password = request.POST.get('password')
        

        

        user = auth.authenticate(username=username,password=password)

        if user is not None:

                auth.login(request,user)
                return redirect('home')
        else:

                messages.info(request,'invalid user and password')
                return redirect('login')
       
    else:

        return render(request,"login.html")


def logout(request):
    if request.session:
        messages.success(request,'succesfully logout')
    else:
        messages.error(request,'session expired login again')
    auth.logout(request)
    return redirect(reverse('login'))

def edit(request):
    if request.method=='POST':
        user = User.objects.get(username=request.user.username)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')
    else:
        return render(request,"edit.html")
def delete(request):
    if request.method=='POST':

        user = User.objects.get(username=request.user.username)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.delete()
        return redirect('logout')
    
   
    return render(request,"profile.html")
def profile(request):

    permission_classes =[IsAuthenticated]

    return render(request,"profile.html")


