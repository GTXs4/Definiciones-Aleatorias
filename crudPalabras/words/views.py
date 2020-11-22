from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from .forms import CreateWordForm, UpdateWordForm, UpdateCategoryForm
from .models import Word, Category, Context, Definition
from django.http import Http404
import random

# Create your views here.

def createword(request):
    words_form = CreateWordForm()

    # Si no existe ninguna categoria o contexto, crea el primero por defecto
    if Category.objects.count() == 0:
        Category.objects.create(category="Sin categoría")
    if Context.objects.count() == 0:
        Context.objects.create(context="Sin contexto")
    categories = Category.objects.all()[:10] # Solo pasaremos los primeros 10 elementos para el datalist del template

    if request.method == "POST":
        words_form = CreateWordForm(data = request.POST) # Con esto estamos rellenando el formulario, para luego comprobar si es valido
        if words_form.is_valid(): # is_valid devolvera True si todos los campos estan rellenados correctamente
            word = words_form.cleaned_data['word'] # otra forma es hacer: request.POST.get('word', '')
            category = words_form.cleaned_data['category'].replace("_", " ").strip().capitalize()
            context = words_form.cleaned_data['context'].replace("_", " ") 
            meaning = words_form.cleaned_data['meaning'] 
            example_en = words_form.cleaned_data['example_en'] 
            example_sp = words_form.cleaned_data['example_sp'] 

            # El siguiente if es solo una solucion momentanea para el acento de categoria en particular
            if category == 'Sin categoria':
                category = "Sin categoría"

            # Aqui intentamos añadir los datos a la BD
            try:
                word1, word_created = Word.objects.get_or_create(word=word.strip().capitalize())
                category1, category_created = Category.objects.get_or_create(category=category)
                context1, context_created = Context.objects.get_or_create(context=context.strip().capitalize())
                meaning = meaning.strip().capitalize()

                if example_en:
                    example_en = example_en.strip().capitalize()
                else:
                    example_en = "No example :("
                if example_sp:
                    example_sp = example_sp.strip().capitalize()
                else:
                    example_sp = "Sin ejemplo :("
                
                # Si la palabra ya existe, no se creara denuevo y seras redireccionado
                if Definition.objects.filter(word=word1).filter(category=category1).filter(context=context1):
                    #print(word1, category1, context1)
                    return redirect(reverse('createword') + '?exists')
                Definition.objects.create(word=word1, category=category1, context=context1, meaning=meaning, example_eng=example_en, example_spa=example_sp)
                return redirect(reverse('createword') + '?ok')
            except:
                return redirect(reverse('createword') + '?fail')

    return render(request, "words/createword.html", {'form':words_form, 'categorias':categories})

class ReadWord(TemplateView):
    template_name = "words/readword.html"

def random_word(request):
    n = Word.objects.count()
    m = Definition.objects.count()
    # Si no hay ninguna palabra o definicion, has lo siguiente
    if n == 0 or m == 0:
        return JsonResponse([{'word':''}], safe=False) # Como no pueden haber palabras vacias, devolveremos una 

    index = random.randint(1,n)
    chosen_word = Word.objects.all()[index-1]  # Nota: Si quieres el id, has chosen_word.id
    definitions = Definition.objects.filter(word=chosen_word)
    # print(index, len(definitions))
    while len(definitions) < 1:
        index = random.randint(1,n)
        chosen_word = Word.objects.all()[index-1] # Nota: esto es como usar las clausulas LIMIT y OFFSET en sql
        definitions = Definition.objects.filter(word=chosen_word)
        #print(index, len(definitions))
    json_response = []
    for definition in definitions:
        json_response.append({'word':definition.word.word, 'category':definition.category.category, 'context':definition.context.context, 'meaning':definition.meaning,
        'example_en':definition.example_eng, 'example_sp':definition.example_spa})
    #json_response = {'word':'Calamar'}
    return JsonResponse(json_response, safe=False)

class ModifyDefinition(TemplateView):
    template_name = "words/modify_definition.html"

def search_definitions(request, word):
    
    definitions = Definition.objects.filter(word__word = word.strip().capitalize())

    json_response = []
    if definitions:
        for definition in definitions:
            json_response.append({'meaning':definition.meaning, 'category':definition.category.category, 'context':definition.context.context, 'id':definition.id})
    else:
        return JsonResponse([{'meaning':''}], safe=False) # Como no pueden haber significados vacios, devolveremos uno 
    return JsonResponse(json_response, safe=False)

class UpdateWord(UpdateView):
    model = Definition
    form_class = UpdateWordForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('updatedefinition', args=[self.object.id]) + '?ok'

class DeleteWord(DeleteView):
    model = Definition
    success_url = reverse_lazy('readword')

class CategoryListView(ListView):
    model = Category

class UpdateCategory(UpdateView):
    model = Category
    form_class = UpdateCategoryForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('updatecategory', args=[self.object.id]) + '?ok'
    
    def get_object(self):
        obj = super(UpdateCategory, self).get_object()
        # No permitiremos que se pueda actualizar la categoria inicial "Sin categoría"
        if obj.category == 'Sin categoría':
            raise Http404()
        return obj