from django.shortcuts import render

# Create your views defhere.
def home(request):
    return render(request, 'pages/home.html')
