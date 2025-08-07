from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def base(request):
    return render(request,'home/base.html')

def hello(request):
    # return HttpResponse("<h1>hello this will working finse</h1>")
    return render(request, 'home/base.html')

def about(request):
    data = ["gaurav", "saurav", "sachin"]
    context = {"list_data": data}  # Key must be a string
    return render(request, 'home/about.html', context)

def home(request):
    return render(request, 'home/home.html')


def testing():
    print("what is going on bro how the josh")

#hello world this commit is done by gaurav branch okk 
def gaurav():
    print("gaurav branch is working on bro !!")