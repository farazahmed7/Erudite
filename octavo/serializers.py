from .models import Subject
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('sub',)
		
