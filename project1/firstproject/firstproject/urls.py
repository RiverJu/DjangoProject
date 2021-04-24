from django.contrib import admin
from django.urls import path, include
from firstapp import views as fa
from wordCount import views as wc #as를 해주는 이유 -> views라고만 표현하면 나중에 다른 앱들이랑 헷갈릴 수 있음.
#media 파일 -> url 설정
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fa.welcome, name="welcome"),
    path('hello/', fa.hello, name="hello"),
    path('wordCount/', wc.home, name="wordCount"),
    path('wordCount/result/', wc.result, name="result"), #home.html의 form태그에서 result로 보내는걸로 해서 name은 result가 되야함.
    path('', include('blog.urls')), #blog앱에서 만든 urls.py include
    path('', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media 파일
