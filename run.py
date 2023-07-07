import gspread
from google.oauth2.service_account import Credentials


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
    while True:
        print("")
        print("Enter how many people serves.\n")
        print("serves must be a number, ie 2\n")

        try:
            serves = int(input("Enter serves here:\n"))
        except ValueError:
            print("Invalid entry. Please try again.")
            continue
        if serves < 0:
            print("Sorry, serves must not be a negative number.")
            continue
        else:
            break

    return serves


def get_ingredients_list():

    ingredients_list = []
    print("")
    print("Enter the ingredients seperated by comma.\n")
    print("Exapmple: eggs, flour, cream\n")
    ingredients = input("Enter the ingredients here:\n")
    ingredients_list.append((ingredients))
    return ingredients_list


def get_instructions():

    instructions_list = []
    print("")
    print("Enter the instructions seperated by comma.\n")
    print("Exapmple: Beat the eggs in a bowl, add the cheese,"
          "cut the bacon in cubes and fry it, add the bacon to the bowl,"
          "boil the pasta, add the pasta in the bowl and stir\n")
    instructions = input("Enter the instructions here:\n")
    instructions_list.append(instructions)
    return instructions_list


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
