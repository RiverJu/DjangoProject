from django.db import models

# Create your models here.
class Blog(models.Model): #상속을 받는다는 의미? 모델이라는 클래스의 속성(메소드)를 그대로 사용할 수 있는 것
    #데이터베이스에서 id라는 column이 있는데 왜 안만들어주는지? 상속받은 Model이라는 클래스 안에 의미 id가 정의되어져 있음.
    title = models.CharField(max_length=200) #models라는 모델에서 가져오기
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField() #본문
    image = models.ImageField(upload_to = "blog/", blank=True, null=True) #upload_to : 업로드할 폴더를 지정하는 것. 
    #settings.py에 media_url로 지정해둔 media 폴더 안에 blog 폴더를 만들어서 관리하겠다는 설정.

    def __str__(self): #str은 class를 하나 만들 때, 어디선가 객체가 호출이 되었을 때 나오는 이름표
        return self.title #메소드가 호출되었을 때 제목을 보여주도록 만듬.
    
    def summary(self): #요약해주는 메소드 사용
        return self.body[:50]
