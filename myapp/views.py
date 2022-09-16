from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html',{})

def pages_blank(request):
    return render(request, 'pages.blank.html', {})

def pages_contact(request):
    return render(request, 'pages_contact.html', {})

def pages_error(request):
    return render(request, 'pages_error.html', {})

def pages_faq(request):
    return render(request, 'pages_faq.html', {})

def pages_login(request):
    return Render(request, 'pages_login.html', {})

def pages_register(request):
    return render(request, 'pages_register.html', {})

def tables_data(request):
    return render(request, 'tables_data.html', {})

def tables_general(request):
    return render(request, 'tables_general.html', {})

def users_profile(request):
    return render(request, 'users_profile.html', {})