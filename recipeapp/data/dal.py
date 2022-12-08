import pyodbc
from ..settings import CONNECTION_STRING
from .. import helpers
from .validation import httprequestvalidation

def find_recipes_for_ingredient(selected_ingredients):

    conn = CONNECTION_STRING
    cursor = conn.cursor()
    recipe_titles = []

    result = helpers.sql_query_select_recipe_by_ingredients(selected_ingredients, cursor)

    if result == None:
        recipe_titles.append("No recipes match")
    else:
        for r in result:
            recipe_titles.append(r.Title)
            
    cursor.close()
    return recipe_titles

def find_method_for_recipe(recipe):
    httprequestvalidation.guard_is_element_string(recipe)
    conn = CONNECTION_STRING
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM Recipes WHERE Title = ?""", recipe)
    result = cursor.fetchone().Method
    cursor.close()

    if result == None:
        return 'Recipe not found'
    else:
        return result

