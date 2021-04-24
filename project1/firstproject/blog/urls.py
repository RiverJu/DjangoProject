from django.contrib import admin #blog 앱에 왜 admin이 필요없는거지..?
from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', blog, name="blog"),
    path('blog/<str:id>', detail, name="detail"), #데이터베이스의 아이디값. str -> 자료형 id -> 매개변수로 지정한 이름
    path('blog/new/', new, name="new"),
    path('blog/create/', create, name="create"),
    path('blog/edit/<str:id>', edit, name="edit"),
    path('blog/update/<str:id>', update, name="update"),
    path('blog/delete/<str:id>', delete, name="delete"),

]