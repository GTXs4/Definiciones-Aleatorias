from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=100, unique=True, verbose_name="Palabra")

    class Meta:
        verbose_name = "Palabra"
        verbose_name_plural = "Palabras"
    
    def __str__(self):
        return self.word 

class Category(models.Model):
    category = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    abbreviation = models.CharField(max_length=50, blank=True, null=True, verbose_name="Abreviatura")
    description = models.TextField(null=True, blank=True, verbose_name="Descripcion")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.category
    
    def underscore_category(self):
        return self.category.replace(" ","_")

class Context(models.Model):
    context = models.CharField(max_length=100, unique=True, verbose_name="Contexto")

    class Meta:
        verbose_name = "Contexto"
        verbose_name_plural = "Contextos"
    
    def __str__(self):
        return self.context

DEFAULT_ID = 1
class Definition(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, verbose_name="Palabra")    
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, default=DEFAULT_ID, verbose_name="Categoria")
    context = models.ForeignKey(Context, on_delete=models.RESTRICT, default=DEFAULT_ID, verbose_name="Contexto")    
    meaning = models.CharField(max_length=150, verbose_name="Significado")
    example_eng = models.TextField(blank=True, null=True, verbose_name="Ejemplo en ingles")
    example_spa = models.TextField(blank=True, null=True, verbose_name="Ejemplo en español")

    class Meta:
        verbose_name = "Definicion"
        verbose_name_plural = "Definiciones"

    def __str__(self):
        return self.meaning