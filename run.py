import gspread
from google.oauth2.service_account import Credentials
import pprint


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
    recipes = data.get_all_records()
    print("Welcome!\n")
    message = "Please choose one of the following."
    user_input_menu(message)


def user_input_menu(message):
    while True:
        try:
            print(f"{message}\n")
            print(f"1: Create a new recipe", "2: Open recipes", "3: Exit\n")
            user_input = int(input("Enter your option here:\n"))
            if user_input == 1:
                create_recipe()
            elif user_input == 2:
                print_recipes()
            elif user_input == 3:
                exit()
            else:
                print("Input out of range. Please try again.\n")
        except ValueError:
            print("Invalid entry. Please try again.\n")


def get_recipe_name():
    """
    Get user input for name, serves, ingredients and instructions.
    Store these values in a list and return this list
    """
    column = data.col_values(1)
    while True:
        name = input("Enter the name of the recipe here:\n")
        if name in column:
            print("Recipe already in library. "
                  "Please choose a different name\n")
        else:
            return name


def get_serves_number():
    print("")
    print("Enter how many people serves.\n")
    print("serves must be a number, ie 2\n")
    serves = validate_int_input("serves")

    return serves


def validate_int_input(list_item):
    while True:
        try:
            user_input = int(input(f"Enter {list_item} here:\n"))
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

    print('Enter the ingredients & quantity\n')
    print("quantity must be a number.\n")

    ingredients = {}
    while True:
        ingredient = input("Enter the ingredient here:\n")
        quantity = validate_int_input("quantity")

        print(f"You have entered {ingredient} : {quantity}\n")
        if ingredient not in ingredients:
            ingredients[ingredient] = quantity
            print(f"Your ingredients list : {ingredients}\n")
        else:
            print("This ingredient is already in your list.\n")
            print(f"Your ingredients list : {ingredients}\n")

        
        end = add_another_item("ingredient")
        if end == False:
            return ingredients


def get_instructions():

    instructions_list ={}
    print("")
    print("Enter the instructions for each step.\n")
    
    step_index = 0
    while True:
        step_index += 1
        instructions = input(f"Enter step {step_index} here:\n")
        instructions_list[f"Step {step_index}"] = instructions
        
        print(instructions_list)
        
        end = add_another_item("step")
        if end == False:
            return instructions_list


def add_another_item(value):
    while True:
        print(f"Would you like to add another {value} y/n\n")
        user_option = input("Enter you option here:\n")
        if user_option.lower() == "y":
            break
        elif user_option.lower() == "n":
            return False
        else:
            print("Please try again.\n")


def create_recipe():
    name = get_recipe_name()
    serves = get_serves_number()

    ingredients = get_ingredients_list()
    instructions = get_instructions()
    recipe_list = []

    recipe_list.append(name)
    recipe_list.append(serves)
    recipe_list.append(str(ingredients))
    recipe_list.append(str(instructions))

    print("Adding to the library...\n")
    data.append_row(recipe_list)
    print(f"Your recipe :\n{recipe_list}\n")
    recipe_list.clear()
    message = "What would you like to do next?"
    user_input_menu(message)


def print_recipes():
    recipes = data.get_all_records()
    column = data.col_values(1)
    empty_list_message = "Your list is empty. Please create a new recipe."
    while len(column) <= 1:
        user_input_menu(empty_list_message)
    message = "What would you like to do next?"
    while True:
        try:
            for i in column:
                index = column.index(i)
                print(f"{index}: {i}")
            print("Please choose a recipe to open by "
                  "inserting the corresponding number\n")
            recipe_index = int(input("Enter your option here:\n"))
            correct_index = recipe_index - 1
            if correct_index in range(len(recipes)):
                print("")
                print(recipes[correct_index])
                user_input_menu(message)
            else:
                print("Input out of range! Please try again.\n")
        except ValueError:
            print("Invalid entry. Please try again.\n")


def main():
    """
    Run all program functions
    """
    choose_open_or_new()


main()
