from django.shortcuts import render

def oddeven(request):
    return render(request,"programs/oddeven.html")

def prime(request):
    return render(request,"programs/prime.html")

def Nprime(request):
    return render(request,"programs/first n prime no.html")

def factors(request):
    return render(request,"programs/factors.html")

def gcd(request):
    return render(request,"programs/gcd.html")

def lcm(request):
    return render(request,"programs/lcm.html")

def eucline(request):
    return render(request,"programs/eucline.html")

def dict(request):
    return render(request,"programs/dictionary.html")

def list(request):
    return render(request,"programs/list.html")

