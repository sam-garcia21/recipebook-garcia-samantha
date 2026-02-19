from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 

from .models import Recipe

# Create your views here.

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes_list": recipes}
    return render(request, 'recipe_list.html', ctx)

def recipe_detail(request, id):
    ctx = { "recipe": Recipe.object.get(pk=pk) }
    return render(request, 'recipe_detail.html', ctx)

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"
