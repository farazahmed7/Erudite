from .models import Search,Genre
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)
		
