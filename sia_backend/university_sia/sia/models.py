from django.db import models

# Modelo Profesor
class Professor(models.Model):
    full_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.full_name

# Modelo Estudiante
class Student(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)  # Asegúrate de encriptar la contraseña en un entorno real
    
    def __str__(self):
        return self.name

# Modelo Asignatura
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

# Modelo Nota
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __str__(self):
        return f'{self.student.name} - {self.subject.name}: {self.grade}'
