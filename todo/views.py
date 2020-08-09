from django.shortcuts import render

# Create your views here.
from rest_framework  import viewsets
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet): # model에 선언되어있는 class를 그대로 사용
    queryset = Todo.objects.all() # 가져오는 데이터를 명시 해준 것
    serializer_class = TodoSerializer # serializer해주는 class를 지정
