from django.contrib import admin

from .models import Recipe, RecipeIngredient, Ingredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline]

    search_fields = ('name',)

    list_display = ('name',)

    list_filter = ('name',)

    fieldsets = [
        ('Details', {
            'fields': [
                'name', 
            ]
        })
    ]

admin.site.register(Recipe, RecipeAdmin)

# Register your models here.
