from django.shortcuts import render

def register(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'index.html')

def sales(request):
    return render(request, 'sales.html')

def purchase(request):
    return render(request, 'purchase.html')
