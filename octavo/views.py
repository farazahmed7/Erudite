from django.shortcuts import render
from .models import Search,Subject,Genre
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST', ])	
def showSubjects(request):
	if request.method=="Post":
			_stream=str(request.POST['stream'])
			_sem=str(request.POST['sem'])
			if _stream=="B.Tech CS" and sem=="":
				a=Genre.objects.get(name="BtechCS").get_children()
				ser=UserSerializer(a,many=True)
				return Response(ser.data)
				
			
			if _stream=="B.Tech CS" and sem=="1":
				a=Genre.objects.get(name="1").get_children()
				ser=UserSerializer(a,many=True)
				return Response(ser.data)				
				
				