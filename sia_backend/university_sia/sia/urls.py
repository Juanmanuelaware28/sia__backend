from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessorViewSet, StudentViewSet, SubjectViewSet, GradeViewSet, RegisterStudentView, RegisterProfessorView

# Crear el router para las vistas basadas en ViewSets
router = DefaultRouter()
router.register(r'professors', ProfessorViewSet)
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns = [
    path('register/student/', RegisterStudentView.as_view(), name='register_student'),
    path('register/professor/', RegisterProfessorView.as_view(), name='register_professor'),
    path('', include(router.urls)),  # Incluye todas las rutas de los ViewSets
]
