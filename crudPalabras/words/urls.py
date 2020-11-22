from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReadWord.as_view(), name = 'readword'),
    path('create/', views.createword, name = 'createword'),
    path('create/random_word/', views.random_word, name = 'word'),
    path('modify/', views.ModifyDefinition.as_view(), name = 'modifydefinition'),
    path('search/<word>/', views.search_definitions, name = 'searchdefinitions'),
    path('update/definition/<int:pk>/', views.UpdateWord.as_view(), name = 'updatedefinition'),
    path('delete/definition/<int:pk>/', views.DeleteWord.as_view(), name = 'deletedefinition'),
    path('categories/', views.CategoryListView.as_view(), name = 'categories'),
    path('update/category/<int:pk>/', views.UpdateCategory.as_view(), name = 'updatecategory'),
]