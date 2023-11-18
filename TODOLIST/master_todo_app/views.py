from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.
def index(request) :
    user = User.objects.get(username='1')
    todos =TODO.objects.filter(author=user)#.values('content')
    content = {"todos" : todos }
    print( content )
    return render(request, 'master_todo_app/index.html', content)

def createtodo(request) :
    inputs = request.POST['todoContent']
    
    # 슈퍼유저 '1'의 사용자 인스턴스를 가져옴
    author = User.objects.get(username='1')
    
    # TODO 모델 인스턴스 생성
    new_todo = TODO(author=author, content=inputs)
    new_todo.save()
    
    return HttpResponseRedirect(reverse('index'))


# 삭제 기능을 가진 View 함수
def deletetodo(request) :
    delete_todo_id = request.GET['todoNum']
    print("fdsfsdfdffsdfsddf", delete_todo_id)
    print("삭제할 TODO ID : ", delete_todo_id)

    user = User.objects.get(username='1')
    todo = TODO.objects.filter(author=user, id=delete_todo_id,)
    todo.delete()

    return HttpResponseRedirect( reverse('index') )




