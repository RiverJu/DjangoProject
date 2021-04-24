from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, "welcome.html")

def hello(request):
    userName = request.GET['name'] #welcome.html에서 form으로부터 name을 받아와서 userName변수에 담음.
    return render(request, "hello.html", {'userName':userName}) #userName변수에서 받은 값을 키인 userName과 매치한다