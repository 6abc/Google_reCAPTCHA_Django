import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages

def contact_page(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')

        data = {
            'secret': settings.YOUR_SECRET_KEY_FROM_GOOGLE_RECAPTCHA_ADMIN_PANEL, 
            'response': recaptcha_response
        }
        verify_url = 'https://www.google.com/recaptcha/api/siteverify'
        response = requests.post(verify_url, data=data)
        result = response.json()

        if result.get('success'):
         
            return redirect('success')

        else:
            messages.error(request, 'reCAPTCHA verification failed. Please try again.')
    
    return render(request, 'contactus.html')


def success(request):
    return render(request, "success.html")
