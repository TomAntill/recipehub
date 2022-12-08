def sql_query_select_recipe_by_ingredients(ingredients, cursor):
    placeholders = ", ".join(["?"] * len(ingredients))

    cursor.execute("""SELECT DISTINCT r.* FROM Ingredients AS i
                            INNER JOIN IngredientsLists AS il ON il.IngredientId = i.Id
                            INNER JOIN RecipeIngredientsLists AS ril ON ril.Id = il.RecipeIngredientsListId
                            INNER JOIN Recipes AS r ON r.RecipeIngredientsListId = ril.Id
                            WHERE IngredientName IN (""" + placeholders + ")" +
                            """AND r.Id NOT IN (SELECT r2.Id FROM Recipes AS r2 
                            INNER JOIN RecipeIngredientsLists AS ril2 ON ril2.Id = r2.RecipeIngredientsListId
                            INNER JOIN IngredientsLists AS il2 ON il2.RecipeIngredientsListId = ril2.Id
                            INNER JOIN Ingredients AS i2 ON i2.Id = il2.IngredientId
                            WHERE i2.IngredientName NOT IN (""" + placeholders + "))""", ingredients + ingredients)
    result = cursor.fetchall()
    return result