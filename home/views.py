from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse, resolve


def home(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(f'{subject}', f'Message from: {email}, {name}\nMessage: {message}', 'emailsenders96@gmail.com',
                  [f'{email}'])
        sent = True
        messages.success(request, 'Thank you for your message, we will answer soon!')
        return redirect('/#contact')
    return render(request, 'home/home.html')
