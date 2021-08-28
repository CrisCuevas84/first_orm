from django.db import models

# Create your models here.
    
class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self): # Podemos sobreescribir el método 
        return "Title: {}".format(self.title) # en escencia acá sobreescribe el modelo a un string (para no ver el diccionario)

