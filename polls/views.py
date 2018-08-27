from django.http import HttpResponse

from django.shortcuts import render

from django.core.cache import cache
from django_redis import get_redis_connection

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
    conn = get_redis_connection('default')

    conn.set("name", '你好')
    name = conn.get("name")

    del conn 

    return render(request, 'polls/hello.html', {'name': name.decode('utf-8')})