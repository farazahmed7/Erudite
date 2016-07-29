from django.shortcuts import render
from .models import Search,Subject
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
	if request.method=="POST":
		_sem=str(request.POST['sem'])
		a=Search.objects.get(sem=_sem)
		if (a.sem=="1"):	
				b=Subject.objects.all()
				ser=UserSerializer(b,many=True)
				return Response(ser.data)
	return HttpResponse("not saved")