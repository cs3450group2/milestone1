from django.shortcuts import redirect, render

# Create your views here.

def register(request):
    if request.method == "POST":
        return redirect('/', permanent=False)
    return render(request, "register.html")

def login(request):
    return render(request, 'login.html')

def index(request):
    return redirect('login/', permanent=False)