from recipeapp import views
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('getRecipesByIngredients',views.get_recipes_by_ingredients),
    path('getMethodForRecipe',views.get_method_for_recipe),
]

