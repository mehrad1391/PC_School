from rest_framework import serializers
from .models import *

class courseserializersapiview(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        
class sessionsserializersapiview(serializers.ModelSerializer):
    class Meta:
        model = session
        fields = '__all__'