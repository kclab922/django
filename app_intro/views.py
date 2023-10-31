from django.shortcuts import render
import random
from faker import Faker

# Create your views here.

def index(request):
    return render(request, 'index.html')

def hello(request):
    username = '최하은'

    result = {
        'username': username,
    }
    # render: 여러 재료들을 섞어 하나의 완성된 html을 만듦
    # result에 들어있던 username이라는 정보를 requst와 hello.html에 적용
    return render(request, 'hello.html', result)

def dinner(request):
    menus = ['라면', '김밥', '떡볶이']
    pick = random.choice(menus)

    result = {
        'pick': pick,
    }

    return render(request, 'dinner.html', result) 


def lotto(request):
    lucky = random.sample(range(1,46),6)

    result = {
        'lucky': lucky,
    }
    return render(request, 'lotto.html', result)   


def greeting(request, name):

    result = {
        'name': name
    }
    return render(request, 'greeting.html', result)


def cube(request, num):

    result = {
        'num': num,
        'cube': num**3,
    }

    return render(request, 'cube.html', result)


def posts(request):
    posts = []

    fake = Faker()

    for i in range(100):
        posts.append(fake.text())

    result = {
        'posts': posts,
    }

    return render(request, 'posts.html', result)