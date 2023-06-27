from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def Home(request):
#     return HttpResponse("""<h1>Hello World</h1>
#     <p style="color:red">This is a paragraph</p>
#     <a href="https://www.google.com">Google</a>""""")
# or make template in folder templates

# def Home(request):
#     return HttpResponse("This is a page")

def index(request):

    # return render(request,'index.html')
    # return render(request,'index.html')


def About(request):
    return HttpResponse("<h1>About</h1>")
