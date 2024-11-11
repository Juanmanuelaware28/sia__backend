from rest_framework import serializers
from .models import Professor, Student, Subject, Grade

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'full_name']

class SubjectSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer()  # Profesor como campo anidado

    class Meta:
        model = Subject
        fields = ['id', 'name', 'code', 'professor']

    def create(self, validated_data):
        professor_data = validated_data.pop('professor')
        professor = Professor.objects.create(**professor_data)  # Crear el profesor si no existe
        subject = Subject.objects.create(professor=professor, **validated_data)
        return subject
    
# Serializador para el Estudiante
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'code', 'password']

# Serializador para la Nota
class GradeSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = Grade
        fields = ['id', 'student', 'subject', 'grade']
