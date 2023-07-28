from django.db import models

class Autor(models.Model):
    nome_autor = models.CharField(max_length=255)
    email_autor = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome_autor
    class Meta:
        verbose_name_plural = "Autores"