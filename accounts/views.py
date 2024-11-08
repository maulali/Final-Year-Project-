from django.shortcuts import render
from .models import Person
from django.http import JsonResponse
from bson import ObjectId
from django.forms.models import model_to_dict



def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def contactus_view(request):
    return render(request, 'contactus.html')

def addperson_view(request):
    return render(request, 'addperson.html')

# def dashboard_view(request):
#     return render(request, 'dashboard.html')


def dashboard_view(request):
    persons = Person.objects.all()  # Fetch all persons from the MongoDB collection
    print('all persons', persons)
    return render(request, 'dashboard.html', {'persons': persons})


def about_view(request):
    return render(request,"about.html")


def persondetails_view(request):
    persons = Person.objects.all()  # Fetch all persons from the MongoDB collection
    return render(request, 'persondetails.html', {'persons': persons})

def apply_filters(request):
    if request.method == 'POST':
        year = request.POST.get('year', None)
        region = request.POST.get('region', None)
        category = request.POST.get('category', None)
        gender = request.POST.get('gender', None)
        location = request.POST.get('location', None)
        age = request.POST.get('age', None)
        qualifications = request.POST.get('qualifications', None)
        job_details = request.POST.get('job_details', None)
        
        # print('year in console...', request.POST)
        filters = {
            **({'year': year} if year else {}),
            **({'region': region} if region else {}),
            **({'category': category} if category else {}),
            **({'gender': gender} if gender else {}),
            **({'location': location} if location else {}),
            **({'age': age} if age else {}),
            **({'qualifications': qualifications} if qualifications else {}),
            **({'job_details': job_details} if job_details else {}),
        }

        persons = Person.objects.filter(**filters)  # Apply the filters to MongoDB
        return render(request, 'dashboard.html', {'persons': persons})

def get_data(person):
    person._id = str(person._id)
    return model_to_dict(person)
        

def get_chart_data(request):
    data = [get_data(person) for person in Person.objects.all()]
      # Convert each Person object to dict
    return JsonResponse(data, safe=False)

def welcome_view(request):
    return render(request, 'welcome.html')

def addperson_form(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        aadhar_number = request.POST.get('aadhar-number')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        qualifications = request.POST.get('qualifications')
        job_details = request.POST.get('job-details')
        location = request.POST.get('location')

        # Create a new Person instance and save it to the database
        person = Person(    
            _id=ObjectId(),
            name=name,
            email=email,
            aadhar_number=aadhar_number,
            gender=gender,
            age=age,
            qualifications=qualifications,
            job_details=job_details,
            location=location
        )
        person.save()
        print("person obj2")
        return render(request, 'addperson.html', {'success': True})

    return render(request, 'addperson.html')