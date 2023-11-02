from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "landing_other/home.html")

def prices(request):
    return render(request, "landing_other/prices.html")

def about(request):
    return render(request, "landing_other/about.html")