from django.shortcuts import render

def home(request):
    return render(request, 'student/home.html')

def dashboard(request):
    return render(request, 'student/dashboard.html')

def profile(request):
    return render(request, 'student/profile.html')
