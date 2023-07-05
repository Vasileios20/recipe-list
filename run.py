import gspread
from google.oauth2.service_account import Credentials
import pandas as pd


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

recipes = data.get_all_records()

def choose_open_or_new():
    while True:
        try:
            print("Choose on of the following:")
            print("1: Create a recipe", "2: Open recipes")
            user_input = int(input("Enter your option here:\n"))
            if user_input == 1:
                add_recipe_to_list()
            elif user_input == 2:
                print("recipes()")                
            else:
                print("Please try again")
        except ValueError:
            print("Try again")


def create_recipe():
    """
    Get user input for name, serves, ingredients and instructions.
    Store these values in a list and return this list
    """
    
    recipe_list = []
    print("Welcome!\n")
    name = input("Enter the name of the recipe here:\n")
    recipe_list.append(str(name))
    print("")
    print("Enter how many people serves.\n")
    print("serves should be a number, ie 2\n")
    serves = int(input("Enter serves here:\n"))
    recipe_list.append(serves)
    ingredients_list = []
    print("")
    print("Enter the ingredients seperated  by comma.\n")
    print("Exapmple: eggs, flour, cream\n")
    ingredients = input("Enter the ingredients here:\n")
    ingredients_list.append(str(ingredients))
    recipe_list.append(str(ingredients_list))
    instructions_list = []
    print("")
    print("Enter the instructions seperated by comma.\n")
    print("Exapmple: Beat the eggs in a bowl, add the cheese, cut the bacon in cubes and fry it, add the bacon to the bowl, boil the pasta, add the pasta in the bowl and stir\n")
    instructions = input("Enter the instructions here:\n")
    instructions_list.append(instructions)
    recipe_list.append(str(instructions_list))
    
    return recipe_list


def add_recipe_to_list():
    """
    Add the recipe to the google sheet in a new row
    """
    recipe = create_recipe()
    print("Adding to the library...\n")
    data.append_row(recipe)
    

def main():
    """
    Run all program functions
    """
    choose_open_or_new()    
    

main()