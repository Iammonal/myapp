from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),   # ✅ Correct
    path('myapp/', include('myapp.urls')),   # Example for your app

]
