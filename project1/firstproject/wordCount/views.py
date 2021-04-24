from django.shortcuts import render

#home.html 띄워주기
def home(request):
    return render(request, "home.html")

def result(request):
    sentence = request.GET['sentence']
    wordList = sentence.split()
    wordDict = {}

    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    return render(request, "result.html", {'fulltext':sentence, 'wordcount':len(wordList), 'wordDict':wordDict.items})
    #items -> 딕셔너리에서 key와 vaule 값을 한꺼번에 전달하기위한 메소드를 사용