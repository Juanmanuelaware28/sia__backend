# student_login/serializers.py
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_student', 'is_professor']
        
from rest_framework import serializers
from .models import CustomUser  # Asegúrate de que la ruta sea correcta

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')  # Los campos que quieras retornar

