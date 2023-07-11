# Recipe List

This project has been developed for the PP3 for the Code Institute. It is
a recipe library where you can store and view recipes.

![GitHub contributors](https://img.shields.io/badge/CONTRIBUTORS-1-<RED>) ![PEP8 validation](https://img.shields.io/badge/PEP8-VALIDATED-<GREEN>)

[View the deployed project here](https://recipe-list-3ecfc536592a.herokuapp.com/)

## Contents

* [User Experience (UX)](#user-experience-ux)  
* [Features](#features)
  * [Main Menu](#main-menu)
    * [Create a new recipe](#create-a-new-recipe)
    * [Open recipes](#open-recipes)

# Features

## Main Menu
On the main menu the user can choose to: 1. Create a new recipe, 2. Open recipes' library or 3. Exit the program.

![Main Menu](/documentation/images/features/main_menu.png)

### Create a new recipe
When the user selects to create a new recipe they will be asked to enter the recipe's name.

![Enter recipe's name](/documentation/images/features/recipe_name.png)

Then will be asked to enter how many people the recipe can serve.

![Serves](/documentation/images/features/serves.png)

Next will be asked to add the ingredients. First the ingredient name, then the quantity and finally the measurement type. When the user finishes entering an ingredient, the user will be asked if they want to add another ingredient.

![Enter ingredients](/documentation/images/features/ingredient_quantity_measurement_type.png)

Last the user will be asked to enter the instructions by steps. A message with each step will be printed and when finsihed, the user will be asked if
they want to add another step. If no, the recipe will be printed and the user will be asked what to do next by showing the main menu.

![Enter instructions](/documentation/images/features/instructions_steps.png)

![Recipe finsihed](/documentation/images/features/recipe_finished.png)

## Open Recipes
When the user selects to open the recipes' library, if the library is empty, a message will be printed saying that the library is empty asking to create a new recipe.

![Empty library](/documentation/images/features/test_empty_list.png)

If there is a recipe in the library, a list with recipes will be printed.

![Recipes Library](/documentation/images/features/recipes_library.png)

Here they can choose which recipe to show/print.

![Selected recipe](/documentation/images/features/printed_recipe.png)



