from django.urls import path 
from . import views

app_name = 'myapp'

urlpatterns = [
    # Main / Landing Page
    path('', views.welcome, name='welcome'),
    
    # Auth & Registration
    path('new-candidate/', views.candidateRegistrationForm, name='registrationForm'),
    path('store-candidate/', views.candidateRegistration, name='storeCandidate'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('home/', views.candidateHome, name='home'),
    
    # Exam / Test Flow
    path('test-paper/', views.testPaper, name='testPaper'),
    path('calculate-result/', views.calculateTestResult, name='calculateTest'),
    path('test-history/', views.testResultHistory, name='testHistory'),
    path('result/', views.showTestResult, name='result'),  # Fixed quotes
    path('candidate-home/', views.candidateHome, name='candidateHome'),
    path('show-result/', views.showTestResult, name='showTestResult'),
    
    # Secondary Index View
    path('index/', views.index, name='index'),
]