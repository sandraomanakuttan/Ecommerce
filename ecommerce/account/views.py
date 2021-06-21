from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("ecommerceapp:allProdCat")
        else:
            messages.info(request,"invalid details")
            return redirect("account:login")
    else:
        return render(request,"login.html")
#

def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect("account:register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already registered")
                return redirect("account:register")
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                        password=password1)
                user.save();
                print("user created")
        else:
            print("password not matched")
            return redirect('account:register')
        return redirect("account:login")
    else:
        return render(request,"registration.html")
#
def logout(request):
    auth.logout(request)
    return redirect("ecommerceapp:allProdCat")