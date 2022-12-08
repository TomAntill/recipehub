from recipeapp.data.dal import find_method_for_recipe, find_recipes_for_ingredient
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

@csrf_exempt
@api_view(["POST"])
def get_recipes_by_ingredients(request):
    
    data = find_recipes_for_ingredient(request.data)
    return JsonResponse(data, safe=False)

@csrf_exempt
@api_view(["GET"])
def get_method_for_recipe(request):
    recipe = request.GET.get('recipename')
    data = find_method_for_recipe(recipe)
    return JsonResponse(data, safe=False)



