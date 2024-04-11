import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Customer
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

def account(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            try:
                username = request.POST.get('username')
                password = request.POST.get('password')
                email = request.POST.get('email')
                address = request.POST.get('address')
                phone = request.POST.get('phone')

                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username already taken")
                    return render(request, 'account.html')
                
                otp = str(random.randint(100000, 999999))

                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email
                )
                customer = Customer.objects.create(
                    username=username,
                    user=user,
                    phone=phone,
                    address=address,
                    otp=otp
                )

                subject = 'Your OTP for registration'
                message = f'Your OTP is: {otp}'
                send_mail(subject,message,settings.EMAIL_HOST_USER,[email])

                request.session['otp'] = otp
                request.session['customer'] = customer.username
                return redirect('otp_verification')

            except Exception as e:
                error_message = str(e)
                messages.error(request, error_message)

        elif 'login' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid Credentials')

    return render(request, 'account.html')

def otp_verification(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp == request.session['otp']:
            customer = Customer.objects.get(username=request.session['customer'])
            customer.save()
            del request.session['otp']
            del request.session['customer']
            messages.success(request, "User registered successfully")
            return redirect('account')
        else:
            messages.error(request, "Invalid OTP")

    return render(request, 'verify.html')

def user_logout(request):
    logout(request)
    return redirect('home')