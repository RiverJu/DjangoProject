from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm): #UserCreationForm에 있는 기능을 RegisterForm이 다 상속받음.
    class Meta:
        model = CustomUser #models 파일에 있는 모델 CustomUser을 가져와 model 변수에 넣음
        fields = ['username', 'password1', 'password2', 'nickname', 'location', 'university']