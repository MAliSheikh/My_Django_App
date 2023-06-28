from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from my_project.models import *
# from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'index.html')


def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        # send_mail(
        #     'Subject: ' + name,
        #     msg,
        #     'work97464@gmail.com',
        #     [email],
        #     fail_silently=False,
        # )

    return render(request, 'index.html')

# def show(request):
#     info=contactinfo.objects.all()
#     print(info)
#     return render(request,"show.html",context={'info' : info})
