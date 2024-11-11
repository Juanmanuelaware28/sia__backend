

# student_login/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializer import CustomUserSerializer

# Vista para registrar un nuevo usuario
class RegisterUserView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        is_student = data.get('is_student', False)
        is_professor = data.get('is_professor', False)
        
        # Crear el usuario
        user = CustomUser.objects.create_user(
            username=username, email=email, password=password, is_student=is_student, is_professor=is_professor
        )
        user.save()

        # Serializar y devolver los datos del nuevo usuario
        user_data = CustomUserSerializer(user).data
        return Response({"message": "User created successfully", "user": user_data}, status=status.HTTP_201_CREATED)

# Vista para hacer login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Autenticación
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Si la autenticación es exitosa, devolver el usuario
            user_data = CustomUserSerializer(user).data
            return Response({
                "message": "Login successful",
                "user": user_data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": "Invalid credentials"
            }, status=status.HTTP_400_BAD_REQUEST)
            
            
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializer import CustomUserSerializer  # Serializador que creaste

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Verificar las credenciales
        user = authenticate(request, username=username, password=password)

        if user:
            # Retornar la respuesta con los datos del usuario en formato JSON
            return Response({
                "message": "Login successful",
                "user": CustomUserSerializer(user).data
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

