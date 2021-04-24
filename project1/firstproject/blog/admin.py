from django.contrib import admin
from .models import Blog #models.py의 Blog를 등록을 했다고 알려줘야 함

admin.site.register(Blog)