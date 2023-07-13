import gspread
from google.oauth2.service_account import Credentials
import json


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("recipes_list")

data = SHEET.worksheet("recipes")


def choose_open_or_new():
    """
    Get user input option by inserting a number to
    run the corresponding function
    """
    recipes = data.get_all_records()
    print("Welcome!\n")
    message = "Please choose one of the following."
    user_input_menu(message)


def user_input_menu(message):
    """
    Get user input option by inserting a number to
    run the corresponding function and validate input.
    User input must be a number. Inside the try check
    the input if it's a number and in range, prints
    out of range if not or raises ValueError if it's any
    other character.
    """
    while True:
        try:
            print(f"{message}\n")
            print(f"1: Create a new recipe", "2: Open recipes", "3: Exit\n")
            user_input = int(input("Enter your option here:\n").strip())
            if user_input == 1:
                create_recipe()
            elif user_input == 2:
                get_recipe_index_to_print()
            elif user_input == 3:
                exit()
            else:
                print("Input out of range. Please try again.\n")
        except ValueError:
            print("Invalid entry. Please try again.\n")


def get_recipe_name():
    """
    Get user input for the recipe's name. Checks if
    name is in the list. If there is asks user to enter
    a different name.
    """
    column = data.col_values(1)
    while True:
        print("")
        name = input("Enter the name of the recipe here:\n").strip()
        if name in column:
            print("Recipe already in library. "
                  "Please choose a different name\n")
        else:
            return name


def get_serves_number():
    """
    Get serves number input from the user
    """
    print("")
    print("Enter how many people serves.\n")
    print("serves must be a number, ie 2\n")
    serves = validate_int_input("serves")

    return serves


def validate_int_input(list_item):
    """
    Inside the try check if the input is a possitive number.
    Prints message if input is not a number or if number
    is negative.
    """
    while True:
        try:
            user_input = int(input(f"Enter {list_item} here:\n").strip())
        except ValueError:
            print("Invalid entry. Please try again.\n")
            continue
        if user_input < 0:
            print(f"Sorry, {list_item} must not be a negative number.\n")
            continue
        else:
            break
    return user_input


def get_ingredients_list():
    """
    Get ingredients name, quantity and measurement type input from the user.
    Check if ingredient is already in the list and ask user
    to insert again if there is. When ingredient has been inserted
    asks user to add another ingredient or to continue to the next function.
    Returns the list in json encoding.
    """
    print("")
    print("Enter the ingredients, the quantity and the measurement type "
          "(gr/ml/units).\n")
    print("quantity must be a number.\n")

    ingredients_list = []
    while True:

        ingredients = {}
        ingredient = input("Enter the ingredient here:\n").strip()
        print("")
        quantity_input = validate_int_input("quantity")
        measurement_type = get_measurement_type()

        ingredients["item"] = ingredient
        ingredients["quantity"] = quantity_input
        ingredients["unit"] = measurement_type

        res = [d.get('item', None) for d in ingredients_list]
        if ingredient not in res:
            ingredients_list.append(ingredients)
            print(f"\nYour list: {ingredients_list}\n")
        else:
            print("\nThis ingredient is already in your list.\n")
            print(f"Your list: {ingredients_list}\n")

        end = add_another_item("ingredient")
        if end is False:
            ingr_list = json.dumps(ingredients_list)
            return ingr_list


def get_measurement_type():
    """
    Get measuerement type input from the user.
    Checks if it's a number and in range of options.
    Raise ValueError if it's any other character or prints
    message if it's out of range.
    """
    while True:
        try:
            print("")
            print("Please choose one of the following.\n")
            print("1: gr", "2: ml", "3: units\n")
            measurement_type = int(input("Enter you option here:\n").strip())
            if measurement_type == 1:
                return "gr"
            elif measurement_type == 2:
                return "ml"
            elif measurement_type == 3:
                return ""
            else:
                print("Input out of range. Please try again.\n")
        except ValueError:
            print("Invalid entry. Please try again.\n")


def get_instructions():
    """
    Gets instructions input from the user. Prints the step number
    for every input. Ask the user if they want to add another step.
    Stores instructions in a list.Returns the list in json encoding.
    """

    instructions_list = []
    print("")
    print("Enter the instructions for each step.\n")

    step_index = 0
    while True:
        step_index += 1
        instructions = input(f"Enter step {step_index} here:\n").strip()
        instructions_list.append(instructions)

        print("")
        print(f"{instructions_list}\n")

        end = add_another_item("step")
        if end is False:
            instruction_list_json = json.dumps(instructions_list)
            return instruction_list_json


def add_another_item(value):
    """
    Get user choice input to add another item
    or to continue to the next function. Checks if
    user's input is y or n, if not ask user to try again.
    """
    while True:
        print(f"Would you like to add another {value} y/n\n")
        user_option = input("Enter you option here:\n").strip()
        if user_option.lower() == "y":
            print("")
            break
        elif user_option.lower() == "n":
            return False
        else:
            print("Please try again.\n")


def create_recipe():
    """
    Run functions needed to create a recipe.
    Appends name, serves, ingredients and instructions
    into a list and append this list in a new row in
    google sheet.
    Pretty prints the recipe.
    """
    name = get_recipe_name()
    serves = get_serves_number()

    ingredients = get_ingredients_list()
    instructions = get_instructions()
    recipe_list = []

    recipe_list.append(name)
    recipe_list.append(serves)
    recipe_list.append(str(ingredients))
    recipe_list.append(str(instructions))

    print("")
    print("Adding to the library...\n")
    data.append_row(recipe_list)
    
    # get list of recipes from worksheet
    recipes = data.get_all_values()
    # reverse the list to bring last recipe first in the list
    recipes.reverse()
    # print the first recipe in the list
    print("Your recipe :\n")
    print_recipe(1)

    recipe_list.clear()
    message = "What would you like to do next?"
    user_input_menu(message)


def get_recipe_index_to_print():
    """
    Pretty print the recipe list as in the following example:
       Name
    -----------
    1: recipe1
    2: recipe2
    ...

    If recipe list (google sheet) is empty asks user to create a new recipe.

    Get user option to print recipe selected.

    Inside the try checks if user's input is a number and in range of options.
    Raises ValueError if input is not a number or prints message if negative
    number or out of range.
    """
    recipes = data.get_all_values()
    column = data.col_values(1)
    empty_list_message = "Your list is empty. Please create a new recipe."
    while len(column) <= 1:
        user_input_menu(empty_list_message)
    message = "What would you like to do next?"
    # create a new list of string lengths using a list comprehension
    column_lengths = [len(s) for s in column]
    # get the largest number in the list
    column_max_int = max(column_lengths)

    while True:
        try:
            print("")
            print("   Name")
            print("-" * (column_max_int + 4))
            for i in column[1:]:
                index = column.index(i)
                print(f"{index}: {i}")
            print("Please choose a recipe to open by "
                  "inserting the corresponding number.\n")
            recipe_index = int(input("Enter your option here:\n").strip())

            print("")
            if recipe_index in range(len(recipes)) and recipe_index > 0:
                print("")
                print_recipe(recipe_index)
                user_input_menu(message)
            else:
                print("Input out of range! Please try again.\n")
        except ValueError:
            print("Invalid entry. Please try again.\n")


def print_recipe(recipe_index):
    """
    Given recipe information from Google Sheets in the below format, pretty
    print it out as in the following example:

    Scrambled Eggs
    ----------------

    Ingredients:
        - Eggs - 2
        - Milk - 100ml

    Instructions:
        1. Whisk the eggs and milk in a bowl.
        2. Heat some butter on a pan.
        3. Bla.

    Args:
        recipe_index: index of a recipe from the Google
            Sheets database.
    """
    recipes = data.get_all_values()
    name = recipes[recipe_index][0]
    serves = recipes[recipe_index][1]

    try:
        ingredients = json.loads(recipes[recipe_index][2])
        instructions = json.loads(recipes[recipe_index][3])
    except json.decoder.JSONDecodeError:
        print("There was a problem loading the recipe.\n")

    print(name)
    print("-" * (len(name) + 2))

    print(f"\nserves - {serves}")

    print("\nIngredients:")
    for ingredient in ingredients:
        name = ingredient["item"]
        quantity = ingredient["quantity"]
        unit = ingredient["unit"]
        print(f"- {name} : {quantity}{unit}")

    print("\nInstructions")
    for index, instruction in enumerate(instructions):
        print(f"Step {index + 1}. {instruction}\n")


def main():
    """
    Run all program functions
    """
    choose_open_or_new()


main()
