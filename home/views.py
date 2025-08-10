from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

from home.models import FirstTable, Cars
from home.controllers.test import test

import json

# def makeEntry_to_db(request):
    

# Create your views here.
def base(request):
    return render(request,'home/base.html')

def hello(request):
    # return HttpResponse("<h1>hello this will working finse</h1>")
    return render(request, 'home/signup.html')

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
    entry.save()
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

def show_db_data(request):
    # Access request if needed, e.g., request.method
    try:
        x = FirstTable.objects.get(id=1)
        return HttpResponse(f"This is your data: name: {x.name}, email: {x.email}")
    except FirstTable.DoesNotExist:
        return HttpResponse("No data found for Gaurav.")
    


@csrf_exempt
def validation(request):
    try:
        if request.method == "POST":
            # Parse incoming JSON body
            try:
                data = json.loads(request.body)
                print("data comes from frontend is: ", data)
            except json.JSONDecodeError:
                return JsonResponse({
                    "success": False,
                    "message": "Invalid JSON format"
                }, status=400)

            # Empty body check
            if not data:
                return JsonResponse({
                    "success": False,
                    "message": "No data provided"
                }, status=400)

            # Get the existing record
            try:
                x = FirstTable.objects.get(id =1)
                print(f"data from database name: {x.name}, email : {x.email}")
            except FirstTable.DoesNotExist:
                return JsonResponse({
                    "success": False,
                    "message": "User not found"
                }, status=404)

            # Validate name
            if data.get("username") != x.name:
                return JsonResponse({
                    "success": False,
                    "message": "Name does not match"
                }, status=400)

            # Validate email
            if data.get("email") == x.email:
                return JsonResponse({
                    "success": False,
                    "message": "User already exists with this email"
                }, status=400)

            # If passed all validations
            return JsonResponse({
                "success": True,
                "message": "Validation passed"
            })

        # If request is not POST
        return JsonResponse({
            "success": False,
            "message": "Only POST requests are allowed"
        }, status=405)

    except Exception as e:
        print("Error occurred:", e)
        return JsonResponse({
            "success": False,
            "message": "Internal server error"
        }, status=500)


async def signup(request):
    try:
        if request.method == "POST":
            try:
                data = json.loads(request.body)
                print("Data received from frontend:", data)

                if not all(k in data for k in ["username", "email", "contact", "password"]):
                    return JsonResponse({
                        "success": False,
                        "message": "Missing required fields"
                    }, status=400)

                # Check if user already exists
                user_data = await FirstTable.objects.filter(email=data["email"]).afirst()
                if user_data:
                    return JsonResponse({
                        "success": False,
                        "message": "User already exists"
                    }, status=400)

                # Create new user
                response = await FirstTable.objects.acreate(
                    username=data["username"],
                    email=data["email"],
                    contact=data["contact"],
                    password=data["password"]
                )

                if response:
                    return JsonResponse({
                        "success": True,
                        "message": "Signup successful!"
                    }, status=200)

            except Exception as e:
                print("Exception in request fetch:", e)
                return JsonResponse({
                    "success": False,
                    "message": "An exception occurred"
                }, status=500)

        else:
            return JsonResponse({
                "success": False,
                "message": "Only POST requests are allowed"
            }, status=405)

    except Exception as e:
        print("Internal error:", e)
        return JsonResponse({
            "success": False,
            "message": "Internal server error"
        }, status=500)


def folderr(request):
    return test(request)