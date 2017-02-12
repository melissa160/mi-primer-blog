from django.db import models
from django.utils import timezone


class Post(models.Model):
    # atributos del modelo Post
    author = models.ForeignKey('auth.User')  # este campo se relaciona con la clase auth
    title = models.CharField(max_length=300)  # campo tipo char
    text = models.TextField()  # campo de texto
    created_date = models.DateTimeField(
            default=timezone.now)  # pone la fecha actual
    published_date = models.DateTimeField(  # requiere que el usuario digite la fecha pero puede ser blanco o nulo
            blank=True, null=True)

    # metodo del modelo Post
    def publish(self):  # el self es explicito y se pone en los metodos de una clase (Post)
        self.published_date = timezone.now()  # para el post que estoy llamando con published le coloca la fecha actual
        self.save()  # guarda el self que es la instancia de la clase

    def __str__(self):  # definicion de la forma como quiero ver el post cuando lo imprima
        return self.title
