from django import forms
from .models import Definition, Category

class CreateWordForm(forms.Form):
    word = forms.CharField(label = 'Palabra', required = True, min_length=1, max_length=100, widget=forms.TextInput(
        attrs={'class':'w3-input w3-border'}
    ))
    category = forms.CharField(label = 'Categoria', required = True, min_length=4, max_length=100, widget=forms.TextInput(
        attrs={'class':'w3-input w3-border', 'list':'categorias'}
    ))
    context = forms.CharField(label = 'Contexto', required = True, min_length=4, max_length=100, widget=forms.TextInput(
        attrs={'class':'w3-input w3-border', 'list':'contextos'}
    ))
    meaning = forms.CharField(label = 'Significado', required = True, min_length=1, max_length=150, widget=forms.TextInput(
        attrs={'class':'w3-input w3-border'}
    ))
    example_en = forms.CharField(label = 'Ejemplo_En', required= False, max_length=500, widget = forms.Textarea(
        attrs={'class':'w3-input w3-border', 'rows':3}
    ))
    example_sp = forms.CharField(label = 'Ejemplo_SP', required= False, max_length=500, widget = forms.Textarea(
        attrs={'class':'w3-input w3-border', 'rows':3}
    ))

class UpdateWordForm(forms.ModelForm):

    class Meta:
        model = Definition
        fields = ['meaning', 'example_eng', 'example_spa'] 
        widgets = {
            'meaning': forms.TextInput(attrs={'class':'w3-input w3-border'}),
            'example_eng': forms.Textarea(attrs={'class':'w3-input w3-border', 'rows':3}),
            'example_spa': forms.Textarea(attrs={'class':'w3-input w3-border', 'rows':3}),
        }
    
    def clean_meaning(self):
        return self.cleaned_data['meaning'].capitalize()
    
    def clean_example_eng(self):
        return self.cleaned_data['example_eng'].capitalize()
    
    def clean_example_spa(self):
        return self.cleaned_data['example_spa'].capitalize()

class UpdateCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['category'] 
        widgets = {
            'category': forms.TextInput(attrs={'class':'w3-input w3-border'}),
        }
    
    def clean_category(self):
        category = self.cleaned_data['category'].replace("_", " ").capitalize()
        if category == 'Sin categoria':
            raise forms.ValidationError("Ya existe esta categoria")
        return category