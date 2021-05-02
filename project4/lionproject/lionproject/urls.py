from django.contrib import admin
from django.urls import path
from blog.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('<str:id>', detail, name="detail"),
]
