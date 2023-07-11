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
* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
* [Deployment and Local Development](#deployment-and-local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to fork](#how-to-fork)
    * [How to clone](#how-to-clone)    

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

# Technologies Used

## Languages Used

Python 3.10.6

## Frameworks, Libraries & Programs Used

* [GitHub](https://github.com/) - To save and store files for the app.
* [VSCode](https://code.visualstudio.com/) - Code editor used for local development.
* [GitPod](https://gitpod.io/) - IDE used to create the site.
* [TinyPNG](https://tinypng.com/) - To reduce size of the images.
* [Shields IO](https://shields.io/) - To add badges to README.
* [Heroku](https://www.heroku.com/) - To deploy the app.
---
* [Google Sheets API/ gspread](https://docs.gspread.org/en/latest/) - To Open a spreadsheet, read, write, and format cell ranges.
* [Google Drive API/ Google OAuth 2.0](https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html) - The Google Drive API allows clients to access resources from Google Drive.
* [json](https://docs.python.org/3/library/json.html) - To pretty print recipes


# Deployment and Local Development

## Deployment
The site is deployed using Heroku. Deployed site [Recipe list](https://recipe-list-3ecfc536592a.herokuapp.com/)
* Create a list of requirements 
  * To create a list of requirements, run the following command in the terminal 'Pip3 freeze > requirements.txt'.
  * Once requirements.txt file has been updated you need to commit this and push the changes up to Github.


If you don't already have an account to Heroku, create one [here](https://www.heroku.com/).

* Go to the Heroku dashboard and click the "Create new app" button.
* Name the app. Each app name on Heroku has to be unique.
* Then select your region.
* And then click "Create app".

* Head over to the settings tab.
* In the settings click the button "Reveal Config Vars".
* In the field for key, enter PORT.
* In the field for value, enter 8000.
* Click "Add".
* In the field for key, enter CREDS.
* Go over to your workspace copy the entire creds.json file, and then paste it into the value field.
* Click “Add”.

The next step is to add buildpacks to the application.

* Click "Add buildpack".
* First select the Python buildpack and click "Save changes".
* Then select the node.js buildpack and click "Save changes". (Make sure that the buildpacks are in this  order, with Python on top, and node.js underneath).

* Go to the deploy tab in settings.
* Choose the deployment method.
* Select Github, and confirm to connect to Github.
* Search for the Github repository name.
* Then click "connect".
* Scroll down  and click "Deploy Branch".

## Local Development
### How to fork
To fork the repository :
1. Log in (sign up) to GitHub.
2. Go to the repository for this project [Recipe list](https://github.com/Vasileios20/recipe-list).
3. Click the fork button in the top right corner.

### How to clone
To clone the repository :
1. Log in (sign up) to GitHub.
2. Go to the repository for this project [Recipe list](https://github.com/Vasileios20/recipe-list).
3. Click on the code button, select one of the HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

