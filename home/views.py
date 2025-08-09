from django.shortcuts import render
from django.http import HttpResponse

from home.models import FirstTable, Cars

# def makeEntry_to_db(request):
    

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
    entry = Cars(
    name="Gaurav",
    email="gaurav@example.com",
    age=21,
    phone="9876543210",
    address="Bihar, India"
    )
    # entry.save()
    print("hello the entry us  made", entry.email)
    return render(request, 'home/home.html')


def testing():
    print("what is going on bro how the josh")

#hello world this commit is done by gaurav branch okk 
def gaurav():
    print("gaurav branch is working on bro !!")
    print("testing is done for making commit from one branch and merge with main branch")



    

def insert_data(request):
    FirstTable.objects.create(
        name="Gaurav",
        email="gaurav@example.com",
        age=21,
        phone="9876543210",
        address="Patna"
    )
    return HttpResponse("Data inserted successfully!")