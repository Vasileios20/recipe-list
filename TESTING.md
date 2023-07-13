# Contents 

* [CI python linter](#jshint)
* [Manual Testing](#manual-testing)
* [Bugs](#bugs)
  * [Solved Bugs](#solved-bugs)

## CI Python linter
![](/documentation/images/testing/pep8_linter.png)

## Manual Testing

|Feature|Expected Outcome|Testing Performed|Result|Pass/Fail|
|--|--|--|--|--|

Main Menu
||||||
|--|--|--|--|--|
|Choose one option from the main menu: 1: Create a new recipe 2: Open recipes 3: Exit for exiting the game|Call the corresponding function|Input "1"|Create a recipe function called|[PASS](/documentation/images/features/recipe_name.png)|
||Call the corresponding function|Input "2"|Print recipe function called|[PASS](/documentation/images/features/recipes_library.png)|
||Call the corresponding function|Input "3"|Exited program|PASS|

Main Menu Validation
||||||
|--|--|--|--|--|
|Choose one option from the main menu: 1: Create a new recipe 2: Open recipes 3: Exit for exiting the game|Print message "Input out of range. Please try again"|Entered "4"|Message printed|[PASS](/documentation/images/testing/user_input_name.png)|
||Print message "Input out of range. Please try again"|Entered "-1"|Message printed|[PASS](/documentation/images/testing/user_input_validation_menu_negative.png)|
||Print message "Invalid entry. Please try again"|Entered "A"|Message printed|[PASS](/documentation/images/testing/user_input_validation_main_string.png)|

Create a new recipe
||||||
|--|--|--|--|--|
|Enter recipe name|Save name in a list, call next function(serves)|Entered "Test"|Name saved in a list, serves function called|[PASS](/)|
|Enter serves|Save serves in a list, call next function(get_ingredients)|Entered 2|serves saved in a list, get_ingredients function called|[PASS](/documentation/images/features/serves.png)|
|Enter ingredient name|Store ingredient in a dictionary with key "item", call next function(get_quantity)|Entered "pasta"|Name saved in the dictionary with key "item", get_quantity function called|[PASS](/documentation/images/features/ingredient_quantity_measurement_type.png)|
|Enter quantity|Store quantity in a dictionary with key "quantity", call next function(get_measurement_type)|Entered "500"|Quantity saved in the dictionary with key "quantity", get_measurement_type function called|[PASS](/documentation/images/features/ingredient_quantity_measurement_type.png)|
|Choose measurement type 1: "gr", 2: "ml", 3: "units"| Get the corresponding type, store in a dictionary with key "unit", call next function(add_another_item)|Entered "1"|"gr" saved in the dictionary with key "unit", add_another_item function called|[PASS](/documentation/images/features/ingredient_quantity_measurement_type.png)|
|| Get the corresponding type, store in a dictionary with key "unit", call next function(add_another_item)|Entered "2"|"ml" saved in the dictionary with key "unit", add_another_item function called|[PASS](/documentation/images/testing/validation_measurement_type_ml.png)|
|| Get the corresponding type, store in a dictionary with key "unit", call next function(add_another_item)|Entered "3"|" " saved in the dictionary with key "unit", add_another_item function called|[PASS](/documentation/images/testing/validation_measurement_type_units.png)|
|Add another ingredient y/n|If user enters "y"/"Y" call get_ingredients function|Entered "y"|Function called|[PASS](/documentation/images/testing/validation_add_another_item_y.png)
|Add another ingredient y/n|If user enters "n"/"n" store ingredients dictionary in a list, call function get_instructions|Entered "n"|Ingredients dictionary stored in a list, get_instructions function called|[PASS](/documentation/images/testing/validation_add_another_item_n.png)
|Enter instructions (steps)|Store instructions in a list, call function add_another_item|Entered "Boiled water"|Instruction saved in a list|[PASS](/documentation/images/features/instructions_steps.png)|
|Add another step y/n|If user enters "y"/"Y" call get_instructions function|Entered "y"|Function called|[PASS](/documentation/images/features/instructions_steps.png)
|Add another step y/n|If user enters "n"/"n" store ingredients dictionary in a list, call function get_instructions|Entered "n"|Ingredients dictionary stored in a list, get_instructions function called|[PASS](/documentation/images/features/recipe_finished.png)

Create a new recipe validation
||||||
|--|--|--|--|--|
|Enter name (already in the recipe list)|Print message "Recipe already in library. Please choose a different name"|Entered name already in the list|Message printed|[PASS](/documentation/images/testing/check_same_name_recipe.png)|
|Enter serves|Print message "Sorry, serves must not be a negative number"|Entered -1|Message printed|[PASS](/documentation/images/testing/user_input_validation_serves_test.png)|
|Enter serves|Print message "Invalid entry. Please try again."|Entered "a"|Message printed|[PASS](/documentation/images/testing/user_input_validation_serves_test.png)|
|Enter quantity|Print message "Sorry, quantity must not be a negative number"|Entered -100|Message printed|[PASS](/documentation/images/testing/user_input_validation_quantity.png)|
|Enter quantity|Print message "Invalid entry. Please try again."|Entered "test"|Message printed|[PASS](/documentation/images/testing/user_input_validation_quantity.png)|
|Choose measurement type 1: "gr", 2: "ml", 3: "units"|Print message "Input out of range. Please try again"|Entered "4". Entered "-1"|Message printed|[PASS](/documentation/images/testing/validation_measurement_type_int.png)|
||Print message "Invalid entry. Please try again"|Entered "test"|Message printed|[PASS](/documentation/images/testing/user_input_validation_measurement_type.png)|
|Add another ingredient y/n|Enter anything other then y/n print message "Please try again."|Entered "1". Entered "a"|Message printed|[PASS](/documentation/images/testing/user_input_validation_add_another_item.png)|

Open recipes
||||||
|--|--|--|--|--|
|Empry library|Print message "Your library is empty. Please create a new recipe"|Selected "2" when library(google sheet) was empty|Message printed|[PASS](/documentation/images/features/test_empty_list.png)|

## Bugs

### Solved Bugs
|#|Bug|Solution|
|--|--|--|
|1|I wasn't able to print the last created recipe without exiting the program|The variable recipe_list was global, I had to make it local variable in the function create_recipe() and clear the list before exiting the function|
|2| Recipe's list(variable column) in function get_recipe_index_to_print() printed the list starting from index 0|I had to add the index that I wanted to start from.
``` python
 print("-- Name")
 for i in column[1:]:
    index = column.index(i)
    print(f"{index}: {i}")
```
