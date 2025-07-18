from django.db import models

# Create your models here.

class Post (models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario (models.Model):
    post= models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=50)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor} en {self.post.titulo}"

    
#Tipos de campos adicionales

'''
Charfield = Texto corto con limitante de caracteres
TextField = Texto largo
DateTimeField = Fecha y hora

BooleanField = Booleanos
IntegerField = Números enteros
EmailField = Email o correo válido

ForeingKey = Relacion muchos a Uno
ManyToManyField = Relacion muchos a muchos
'''

#Paso obligatorio despues de manipular los modelos es hacer migraciones

'''
python manage.py makemigrations = crea las migraciones

python manage.py migrate = aplicar los cambios en la base de datos
'''

