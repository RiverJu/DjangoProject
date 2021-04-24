from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog #데이터베이스에서 데이터를 달라고 해야함.(models.py에서 Blog model을 import 해옴.)
#작성한 시간을 저장해주는 모듈 사용
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import BlogForm

def blog(request):
    blogs = Blog.objects.order_by('-pub_date') #Blog모델에 있는 객체들을 싹다 가져와라
    #order_by('-pub_date') -> 최신순으로 나열해줌.
    search = request.GET.get('search')
    if search == 'true':
        author = request.GET.get('writer')
        blogs = Blog.objects.filter(writer=author)
        return render(request, 'blog.html', {'blogs':blogs})

    paginator = Paginator(blogs, 3) #blogs를 3개로 나눠서 보냄
    page = request.GET.get('page') #local host로 들어왔을 때도 보여지는 화면은 같으니깐 .get으로 해줌
    blogs = paginator.get_page(page)
    return render(request, 'blog.html',{'blogs':blogs}) #객체들을 담은 blogs변수를 blog.html에 함께 넘겨줘야함
    #이때 Blog모델에 있던 객체들이 blogs변수에 담겨졌고 이것이 blog.html에 보내질 때 blogs변수에 있던 값이 
    # blogs키에 넣어서 보냄

def detail(request, id): #blog의 아이디를 받아옴.
    #blog = Blog.objects.get(id = id) #id값이 같은 객체를 들고 와라
    blog = get_object_or_404(Blog, pk=id ) #get_object_or_404 -> 객체를 들고오던가 아님 오류페이지를 띄우던가(찾을수 없는 페이지도 해줌)
    #pk = primary key(기본키) -> 데이터들을 구별하는 것
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form':form})

def create(request): #new.html에서 정보가 오기때문에 받아야함.
    #new_blog = Blog() #new_blog는 Blog의 object가 됨
    #new_blog.title = request.POST['title']
    #new_blog.writer = request.POST['writer']
    #new_blog.body = request.POST['body']
    #new_blog.pub_date = timezone.now()
    #new_blog.image = request.FILES['image']
    #new_blog.save()
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False) #임시저장
        new_blog.pub_date = timezone.now()
        new_blog.save()
        #request로 요청을 보냈으니 어떤 화면을 보여줄지 return 
        return redirect('detail', new_blog.id) #새로운 객체의 id값을 detail페이지한테 보내줘야함.
    return redirect('home')


def edit(request, id):
    edit_blog = Blog.objects.get(id= id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id = id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('blog')