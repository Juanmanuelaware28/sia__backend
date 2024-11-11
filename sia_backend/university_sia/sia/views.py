from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Professor, Student, Subject, Grade
from .serializer import ProfessorSerializer, StudentSerializer, SubjectSerializer, GradeSerializer

# Vista para el CRUD de Profesores
class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

# Vista para el CRUD de Estudiantes
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Vista para el CRUD de Asignaturas
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# Vista para el CRUD de Notas
class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

# Vista para registrar un nuevo Estudiante (si es necesario)
class RegisterStudentView(APIView):
    def post(self, request):
        data = request.data
        # Crear un nuevo Estudiante
        student = Student.objects.create(name=data['name'], code=data['code'], password=data['password'])
        return Response({"message": "Student registered successfully"}, status=status.HTTP_201_CREATED)

# Vista para registrar un nuevo Profesor (si es necesario)
class RegisterProfessorView(APIView):
    def post(self, request):
        data = request.data
        # Crear un nuevo Profesor
        professor = Professor.objects.create(full_name=data['full_name'])
        return Response({"message": "Professor registered successfully"}, status=status.HTTP_201_CREATED)
