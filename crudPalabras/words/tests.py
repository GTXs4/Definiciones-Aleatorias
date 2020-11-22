from django.test import TestCase
from .models import Word, Category, Context, Definition

# Create your tests here.
class DefinitionTestCase(TestCase):
    def setUp(self):
        # Nota: Si quieres ahorrar los .get de las pruebas, podrias hacer algo como la linea que sigue, para acceder a los datos con self
        # self.word = Word.objects.create(word='Woodworker')
        Word.objects.create(word='Woodworker')
        Category.objects.create(category='Sin categoria')
        Context.objects.create(context='Sin contexto')
    
    def test_create_definition(self):
        word = Word.objects.get(word='Woodworker')
        category = Category.objects.get(category='Sin categoria')
        context = Context.objects.get(context='Sin contexto')

        definition = Definition.objects.create(word=word, category=category, context=context, meaning='Carpintero')
        print(f'\n la definicion es: {definition.meaning}, de la palabra: {definition.word}, con la categoria: {definition.category}, y el contexto: {definition.context}')
        print(f'id_word: {definition.word_id}, id_category: {definition.category_id}, id_context: {definition.context_id}')
        self.assertEqual(definition.meaning, 'Carpintero')
    
    