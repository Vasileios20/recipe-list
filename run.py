

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


def create_recipe():
    """
    Get user input for name, serves, ingredients and instructions.
    Store these values in a list and return this list
    """
    recipe = []
    print("Welcome!\n")
    name = input("Enter the name of the recipe here:\n")
    recipe.append(str(name))
    print("")
    print("Enter how many people serves.\n")
    print("serves should be a number, ie 2\n")
    serves = int(input("Enter serves here:\n"))
    recipe.append(serves)
    ingredients_list = []
    print("")
    print("Enter the ingredients seperated  by comma.\n")
    print("Exapmple: eggs, flour, cream\n")
    ingredients = input("Enter the ingredients here:\n")
    ingredients_list.append(str(ingredients))
    recipe.append(str(ingredients_list))
    instructions_list = []
    print("")
    print("Enter the instructions seperated by comma.\n")
    print("Exapmple: Beat the eggs in a bowl, add the cheese, cut the bacon in cubes and fry it, add the bacon to the bowl, boil the pasta, add the pasta in the bowl and stir\n")
    instructions = input("Enter the instructions here:\n")
    instructions_list.append(instructions)
    recipe.append(str(instructions_list))
    return recipe


def add_recipe_to_list(recipe):
    """
    Add the recipe to the google sheet in a new row
    """
    print("Adding to the library...")
    data.append_row(recipe)
    

def main():
    """
    Run all program functions
    """
    recipe = create_recipe()
    add_recipe_to_list(recipe)


main()