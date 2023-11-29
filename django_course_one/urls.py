
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_one.urls')),
    path('app_two/',include('app_two.urls')),
]
