from django.shortcuts import render

# Create your views here.

# view for login screen
def login(request):
    return render(request, 'pages/login.html', {}) 