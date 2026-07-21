from django.shortcuts import render 
from django.template import loader 
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import Candidate
from myapp.models import Question
import random

def welcome(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render({}, request)) # Added empty context dict

def candidateRegistrationForm(request):
    return render(request, 'registration_form.html')

def candidateRegistration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        
        # Optimized check: .exists() is faster than len()
        if Candidate.objects.filter(username=username).exists():
            userStatus = 1 # Already exists
        else:
            candidate = Candidate()
            candidate.username = username
            candidate.password = request.POST.get('password')
            candidate.name = request.POST.get('name')
            candidate.save()
            userStatus = 2 # Success
    else:
        userStatus = 3 # Method is not POST
        
    context = {'userStatus': userStatus} 
    return render(request, 'registration.html', context)

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        candidate = Candidate.objects.filter(username=username, password=password)

        if candidate.exists():
            # Login Success
            user_obj = candidate.first()
            request.session['username'] = user_obj.username
            request.session['name'] = user_obj.name
            return render(request, 'home.html', {'name': user_obj.name})  
        else:
            # Login failed (Incorrect credentials)
            return render(request, 'login.html', {'loginError': "Invalid Username or Password"})
            
    # Handles the standard GET request to view the login page
    return render(request, 'login.html')   

def candidateHome(request):
    if 'name' not in request.session:
        return HttpResponseRedirect("login") # Added return here
    
    return render(request, 'home.html')

def testPaper(request):
   if 'name' not in request.session:
        return HttpResponseRedirect("login")
   n=int(request.GET.get('n',0))
   question_pool=list(Question.objects.all())
   random.shuffle(question_pool)
   questions_list=question_pool[:n]
   context={'questions':questions_list}
   res=render(request,'test_paper.html',context)
   return res 


def calculateTestResult(request):
    pass

def testResultHistory(request):
    pass

def showTestResult(request):
    pass

def logoutView(request):
    # flush() removes everything, cleans up the cookie, and deletes session data
    request.session.flush() 
    return HttpResponseRedirect("login")

def index(request):
    return HttpResponse("Welcome to MyApp!")
