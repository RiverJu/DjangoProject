from django.shortcuts import render, get_object_or_404
from .models import Blog #데이터베이스에서 데이터를 달라고 해야함. 

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog':blog})
    