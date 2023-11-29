from django.shortcuts import render

from django.contrib import messages

# Create your views here.
def index(request):
    messages.info(request,"App one index page")

    return render(request, 'app_one/index.html')