from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request) :
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request,user)
            return redirect('cart') 
        else:
           request.session['failed_attempts'] = request.session.get('failed_attempts', 0) + 1
           message = request.session['failed_attempts']                   # stores the session data in message
           return render(request,'login.html',{'error' :message})

    return render(request,'login.html')

def user_logout(request) :
    logout(request)
    return redirect('login')

@login_required
def ViewCart(request) :
    visits = int(request.COOKIES.get('visits',0))  # stores the cookies
    visits = visits+1
    Cart = ['orange','apple']
    response = render(request,'cart.html',{'cart':Cart,'visits':visits})
    response.set_cookie('visits',visits)
    return response