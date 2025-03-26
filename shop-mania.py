"""
Program that generates a shopping list. 
"""

__author__ = "Shravya Chandrasekar"
__date__ = "24/03/2023"

from constants import *


def num_hours() -> float:
    """
    Function that converts the assigned number of estimated hours spent on this
    assignment into a float.

    Parameters: Inputted as an integer.

    Return: Number of hours into a float.

    Example:
    >>> num_hours()
    40.0
    """ 
    return float(40)


def get_recipe_name(recipe: tuple[str, str]) -> str:
    """
    Returns the name of the inputted recipe as a string.

    Parameters: Input recipe as a tuple containing two strings.

    Return: String of recipe name.

    Example:
    >>> get_recipe_name(('chocolate peanut butter banana shake',
    ' 1 large banana,240 ml almond milk'))
    'chocolate peanut butter banana shake'
    """
    recipe = recipe[0]
    return recipe


def parse_ingredient(raw_ingredient_detail: str) -> tuple[float, str, str]: 
    """
    Returns the ingredient breakdown which includes amount, measure and
    ingredient name.

    Parameters: Input is the recipe's ingredients as strings.

    Return: The tuple of the amount as a float, amount and ingredient name
    as a string.

    Example:
    >>> parse_ingredient('0.5 tsp coffee granules')
    (0.5, 'tsp', 'coffee granules')
    """
    # split the raw ingredient into tokens
    result = raw_ingredient_detail.split()
    
    # set default values for the amount, measure, and ingredient
    amount = float(result[0])
    measure = result[1]
    ingredient = ' '.join(result[2:])
    return amount, measure, ingredient


def create_recipe() -> tuple[str, str]:
    """
    Creates a recipe by asking user to input recipe name and as many ingredients
    required. Ingredients are listed with order of amount, measure and name.
    Breaks when ingredient input is empty.

    Parameters: Nothing is to be inputted for function to work. 

    Return: A recipe in tuple format generated from inputs. 

    Example:
    >>> create_recipe()
    Please enter the recipe name: peanut butter
    Please enter an ingredient: 300 g peanuts
    Please enter an ingredient: 0.5 tsp salt
    Please enter an ingredient: 2 tsp oil
    Please enter an ingredient:
    ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    """
    recipe_name = input("Please enter the recipe name: ")
    recipe_ingredients = []
    ingredient = input("Please enter an ingredient: ")
    while ingredient!= "":
        recipe_ingredients.append(ingredient)
        ingredient = input("Please enter an ingredient: ")
    recipe = (recipe_name, ",".join(recipe_ingredients))
    return recipe


def recipe_ingredients(recipe: tuple[str, str]) -> tuple[tuple[float, str, str]]:
    """
    Returns the recipe's ingredients in amount, measure and ingredient name.

    Parameters: Input recipe as a tuple containing two strings.

    Return: Takes the tuple of each ingredient containing amount as a float,
    amount and ingredient name as a string and tuples them together.

    Example:
    >>> recipe_ingredients(('peanut butter','300 g peanuts,
    0.5 tsp salt,2 tsp oil'))
    ((300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'))
    """
    ingredients = recipe[1].split(',')
    ingredient_detail = []
    for ingredient in ingredients:
        result = ingredient.split()
        amount = float(result[0])
        measure = result[1]
        name = ' '.join(result[2:])
        ingredient_detail.append((amount, measure, name))
    return tuple(ingredient_detail)


def add_recipe(new_recipe: tuple[str, str],recipes: list[tuple[str, str]]) -> None:
    """
    An inputted recipe is added into the list of recipes.

    Parameters: Recipe as a tuple containing two strings and recipes as the
    list of recipes.

    Return: None

    Example:
    >>> recipes = []
    >>> recipe = ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    >>> add_recipe(recipe, recipes)
    >>> recipes
    [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')]
    """
    recipes.append(new_recipe)
    
    return None


def find_recipe(recipe_name:str, recipes: list[tuple[str, str]]) -> tuple[str, str] | None:
    """
    Finds a recipe in recipes if provided with recipe name and if contained
    in recipes.

    Parameters: String of recipe name and list of recipes.

    Return: If name of recipe is present in recipes after being added, it will
    return the full recipe. If not, returns None.

    Example:
    >>> recipes = [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')]
    >>> find_recipe('peanut butter', recipes)
    ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    >>> find_recipe('cinnamon rolls', recipes)
    >>> print(find_recipe('cinnamon rolls', recipes))
    None
    """
    for recipe in recipes:
        if recipe_name == recipe[0]:
            return recipe
    return None


def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> None:
    """
    When inputted a recipe name, it removes it from recipes if previously
    added to recipes.

    Parameters: Name of recipe as a string and the list of recipes.

    Return: Returns None.

    Example:
    >>> recipes = [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil'),
    ('cinnamon rolls', '480 ml almond milk,115 g Nuttelex,50 g sugar,7 g
    active dry yeast,5.5 cup flour,1 tsp salt,170 g Nuttelex,165 g brown
    sugar,2 tbsp cinnamon,160 g powdered sugar,30 ml almond milk,0.5 tsp
    vanilla extract')]
    >>> remove_recipe('brownie', recipes)
    >>> recipes
    [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil'), ('cinnamon
    rolls', '480 ml almond milk,115 g Nuttelex,50 g sugar,7 g active dry
    yeast,5.5 cup flour,1 tsp salt,170 g Nuttelex,165 g brown sugar,2 tbsp
    cinnamon,160 g powdered sugar,30 ml almond milk,0.5 tsp vanilla
    extract')]

    >>> remove_recipe('cinnamon rolls', recipes)
    >>> recipes
    [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')]
    """
    for recipe in recipes:
        if name == recipe[0]:
            recipes.remove(recipe)
            return


def get_ingredient_amount(ingredient: str, recipe: tuple[str, str]) -> tuple[float, str] | None:
    """
    Retrieves the ingredient amount and measure from the recipe.
    
    Parameters: Ingredient as a string and recipe as a tuple containing
    two strings.

    Return: If ingredient in present in recipe, it retrieves the amount and
    measure in float and string respectively. If ingredient doesn't exist,
    it returns None and nothing happens. 

    Example:
    >>> recipe = ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    >>> get_ingredient_amount('peanuts', recipe)
    (300.0, 'g')
    >>> get_ingredient_amount('soy beans', recipe)
    """
    ingredients = recipe[1].split(',')
    # Loops through ingredients
    for ing in ingredients:
        amount_unit = ing.split()
        amount = amount_unit[0]
        unit = amount_unit[1]
        name = ' '.join(amount_unit[0:11])
        if ingredient.lower() in name.lower():
            return (float(amount), unit)
    return None


def add_to_shopping_list(ingredient_details: tuple[float, str, str], shopping_list: list[tuple[float, str, str] | None]) -> None:
    """
    Adds an ingredient to the shopping list. If same ingredient is added,
    the amount is combined. If ingredient doesn't previously exist in
    shopping list, it is just added as it is.

    Parameters: Ingredient details as a tuple of amount, meausure and
    ingredient name. Shopping list contains either an empty tuple or
    already inserted ingredient details.

    Return: Returns None.

    Example:
    >>> shopping_list = [(300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'),
    (2.0, 'tsp', 'oil')]
    >>> add_to_shopping_list((1000.0, 'g', 'tofu'), shopping_list)
    >>> shopping_list
    [(300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'),
    (1000.0, 'g', 'tofu')]
    >>> add_to_shopping_list((1200.0, 'g', 'peanuts'), shopping_list)
    >>> shopping_list
    [(1500.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'),
    (1000.0, 'g', 'tofu')]
    >>> add_to_shopping_list((8000.0, 'g', 'tofu'), shopping_list)
    >>> shopping_list
    [(1500.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'),
    (9000.0, 'g', 'tofu')]
    """
    # Goes through each item in the shopping list
    for i, item in enumerate(shopping_list):
        if item and item[2] == ingredient_details[2]:
            shopping_list[i] = (item[0] + ingredient_details[0],
            item[1], item[2])
            break
    else:
        shopping_list.append(ingredient_details)
    return None


def remove_from_shopping_list(ingredient_name: str, amount: float, shopping_list: list) -> None:
    """
    Removes a specific amount of an ingredient from the shopping list.
    If ingredient exists in list, takes away inputted amount from the
    amount in shopping list. If the amount falls below zero, the ingredient
    is fully removed fom shopping list. Break is utilised in the if statement
    when the shopping list amount is greater than amount entered to stop
    from looping. 

    Parameters: Ingredient name as a string, amount as a float and shopping
    list as a list.

    Return: Returns None.

    Example:
    >>> shopping_list = [(1500.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'),
    (2.0, 'tsp', 'oil'), (9000.0, 'g', 'tofu'), (100.0, 'g', 'sugar'),
    (50.0, 'g', 'tomato sauce'), (120.0, 'g', 'rice'),
    (920.0, 'g', 'ice cream')]
    >>> remove_from_shopping_list('ice cream', 500.0, shopping_list)
    >>> shopping_list
    [(1500.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'),
    (9000.0, 'g', 'tofu'), (100.0, 'g', 'sugar'), (50.0, 'g', 'tomato
    sauce'), (120.0, 'g', 'rice'), (420.0, 'g', 'ice cream')]
    >>> remove_from_shopping_list('sugar', 500.0, shopping_list)
    >>> shopping_list
    [(1500.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'),
    (9000.0, 'g', 'tofu'), (50.0, 'g', 'tomato sauce'), (120.0, 'g',
    'rice'), (420.0, 'g', 'ice cream')]
    >>> remove_from_shopping_list('ice cream', 9000.0, shopping_list)
    >>> shopping_list
    [(1500.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'),
    (9000.0, 'g', 'tofu'), (50.0, 'g', 'tomato sauce'), (120.0, 'g',
    'rice')]
    """
    
    for i in range(len(shopping_list)):
        # Checks if ingredient name given is in shopping list
        if shopping_list[i][2] == ingredient_name:
            # If amount greater, takes it away
            if shopping_list[i][0] > amount:
                shopping_list[i] = (shopping_list[i][0]
                - amount, shopping_list[i][1], shopping_list[i][2])
                break
            # If amount equal to or less, removes ingredient from list
            elif shopping_list[i][0] <= amount:
                del shopping_list[i]
                break
    return None


def generate_shopping_list(recipes: list[tuple[str, str]]) -> list[tuple[float, str, str]]:
    """
    Generates a list of ingredients of given recipes.

    Parameters: Recipes are a list of tuple containing two strings.

    Return: Returns the shopping list of ingredients formatted as a list
    of tuples containing float of amount, and strings of measure and ingredient name.

    Example:
    >>> shopping_list = generate_shopping_list([PEANUT_BUTTER,
    MUNG_BEAN_OMELETTE])
    >>> shopping_list
    [(300.0, 'g', 'peanuts'), (1.0, 'tsp', 'salt'), (3.0, 'tsp', 'oil'),
    (1.0, 'cup', 'mung bean'), (0.75, 'tsp', 'pink salt'), (0.25, 'tsp',
    'garlic powder'), (0.25, 'tsp', 'onion powder'), (0.125, 'tsp',
    'pepper'), (0.25, 'tsp', 'turmeric'), (1.0, 'cup', 'soy milk')]
    >>> shopping_list = generate_shopping_list([PEANUT_BUTTER, PEANUT_BUTTER,
    MUNG_BEAN_OMELETTE])
    >>> shopping_list
    [(600.0, 'g', 'peanuts'), (1.5, 'tsp', 'salt'), (5.0, 'tsp', 'oil'),
    (1.0, 'cup', 'mung bean'), (0.75, 'tsp', 'pink salt'), (0.25, 'tsp',
    'garlic powder'), (0.25, 'tsp', 'onion powder'), (0.125, 'tsp',
    'pepper'), (0.25, 'tsp', 'turmeric'), (1.0, 'cup', 'soy milk')]
    """
    # Establish an empty list to store ingredients 
    shopping_list = []
    for recipe in recipes:
        ingredients = recipe[1].split(',')
        for ingredient in ingredients:
            # Split ingredients
            result = ingredient.split()
            # Retrieve amount and measure from ingredient 
            amount = float(result[0])
            measure = result[1]
            ingredient_name = ' '.join(result[2:])
            # False indicates whether ingredient has been found in list
            found = False
            # Goes through each item in the shopping list
            for i, item_data in enumerate(shopping_list):
                if ingredient_name == item_data[2]:
                    # Update shopping list
                    shopping_list[i] = (item_data[0] +
                    amount, item_data[1], item_data[2])
                    found = True
                    break
            if not found:
                shopping_list.append((amount, measure, ingredient_name))
    return shopping_list


def display_ingredients(shopping_list: list[tuple[float, str, str]]) -> None:
    """
    Prints the inputted and updated shopping list according to user.

    Parameters: The shopping list of ingredients formatted as a
    list of tuples containing float of amount, and strings
    of measure and ingredient name.

    Return: Returns None.

    Example:
    >>> display_ingredients([(1.0, 'large', 'banana'), (0.5, 'cup', 'ice'),])
    | 1.0 | large | banana |
    | 0.5 | cup | ice |
    >>> display_ingredients([(1.0, 'large', 'banana'),
    (2.0, 'tbsp', 'peanut butter'),
    (2.0, 'pitted', 'dates'),
    (1.0, 'tbsp', 'cacao powder'),
    (240.0, 'ml', 'almond milk'),
    (0.5, 'cup', 'ice'),
    (1.0, 'tbsp', 'cocao nibs'),
    (1.0, 'tbsp', 'flax seed')])
    |â£â£â£1.0â£|â£â£largeâ£â£|â£bananaâ£â£â£â£â£â£â£â£â£|
    |â£â£â£2.0â£|â£â£tbspâ£â£â£|â£peanutâ£butterâ£â£|
    |â£â£â£2.0â£|â£pittedâ£â£|â£datesâ£â£â£â£â£â£â£â£â£â£|
    |â£â£â£1.0â£|â£â£tbspâ£â£â£|â£cacaoâ£powderâ£â£â£|
    |â£240.0â£|â£â£â£mlâ£â£â£â£|â£almondâ£milkâ£â£â£â£|
    |â£â£â£0.5â£|â£â£â£cupâ£â£â£|â£iceâ£â£â£â£â£â£â£â£â£â£â£â£|
    |â£â£â£1.0â£|â£â£tbspâ£â£â£|â£cocaoâ£nibsâ£â£â£â£â£|
    |â£â£â£1.0â£|â£â£tbspâ£â£â£|â£flaxâ£seedâ£â£â£â£â£â£|
    Output above has visible spaces for better understanding of format.
    """
    # Determines the max width for the three columns
    max_amount_width = max(len(str(item[0])) for item in shopping_list)
    max_measure_width = max(len(item[1]) for item in shopping_list) 
    max_ingredient_width = max(len(item[2]) for item in shopping_list)

    # Prints the table rows for amount, measure and ingredient name
    for item in shopping_list:
        amount_str = f" {item[0]:>{max_amount_width}} "
        measure_str = item[1]
        if len(measure_str) % 2 == 1:
            measure_str = f"  {measure_str:^{max_measure_width}} "
        else:
            measure_str = f" {measure_str:^{max_measure_width}}  "
        ingredient_str = f" {item[2]:<{max_ingredient_width}}  "
        print(f"|{amount_str}|{measure_str}|{ingredient_str}|")
    return None


def sanitise_command(command: str) -> str:
    """
    Autocorrects inputted text by the user. It removes numbers, and leading
    and trailing white spaces.It returns the standardised command to
    all lower-case. Essentially allows user input to be readable
    to functions when recalled.

    Parameters: Command is the input of the user and is formatted as a string.

    Return: Returns as a standardised command.

    Example:
    >>> sanitise_command('add chocolate brownies')
    'add chocolate brownies'
    >>> sanitise_command('add c4hocolate Brownies')
    'add chocolate brownies'
    >>> sanitise_command('add chocolate Brownies 5')
    'add chocolate brownies'
    >>> sanitise_command('add chocolate Brownies ')
    'add chocolate brownies'
    """
    # Converts input to lowercase and removes leading/trailing whitespaces
    command = command.lower().strip()
    # Removes any numbers from the input string
    command = ''.join([char for char in command if not char.isdigit()])
    # Replaces any whitespaces with a single space
    command = ' '.join(command.split())
    return command


def main() -> None:
    """
    The main interaction loop that the user interacts with. Program prompts user
    to enter a command which allows them to navigate and operate the shopping
    list.

    Parameters: The input is prompted by the user and is a string.

    Return: The function returns None. The function breaks when user inputs
    'q' or 'Q'.

    Example:
    Please enter a command: add coconut
    Recipe does not exist in the cook book.
    Use the mkrec command to create a new recipe.
    Please enter a command: rm coconut
    Please enter a command: mkrec
    Please enter the recipe name: coconut
    Please enter an ingredient: 1 large coconut
    Please enter an ingredient:
    Please enter a command: ls
    No recipe in meal plan yet.
    Please enter a command: ls -a
    chocolate peanut butter banana shake
    chocolate brownies
    seitan
    cinnamon rolls
    peanut butter
    omelette
    coconut
    Please enter a command: add coconut
    Please enter a command: ls
    [('coconut', '1 large coconut')]
    Please enter a command: g
    | 1.0 | large | coconut |
    Please enter a command:
    """
    #cook book
    recipe_collection = [
        CHOCOLATE_PEANUT_BUTTER_SHAKE, 
        BROWNIE, 
        SEITAN, 
        CINNAMON_ROLLS, 
        PEANUT_BUTTER, 
        MUNG_BEAN_OMELETTE
    ]
    # Establish an empty lists to store recipes and shopping list 
    recipes = []
    shopping_list = []
    
    while True:
        command = input("Please enter a command: ")
        
        if command == 'h' or command == 'H':
            print("    H or h: Help")
            print("    mkrec: creates a recipe, add to cook book.")
            print("    add {recipe}: adds a recipe to the collection.")
            print("    rm {recipe}: removes a recipe from the collection.")
            print("    rm -i {ingredient_name} {amount}: removes ingredient from shopping list.")
            print("    ls: list all recipes in shopping cart.")
            print("    ls -a: list all available recipes in cook book.")
            print("    ls -s: display shopping list.")
            print("    g or G: generates a shopping list.")
            print("    Q or q: Quit.")

        elif command == 'mkrec':
            # Creates a new recipe and adds it to cook_book
            recipe = create_recipe()
            add_recipe(recipe, recipe_collection)


        elif command.lower().startswith('add'):
            # Sanitises user input
            command = sanitise_command(command)
            # Separates the recipe name given by user
            recipe_name = command[3:].strip()
            found = False
            # Loops through recipe collection
            for recipe in recipe_collection:
                # Checks if recipe name matches recipe name given by user
                if recipe[0].lower() == recipe_name.lower():
                    found = True
                    add_recipe(recipe, recipes)
                    break
            if not found:
                print("")
                print("Recipe does not exist in the cook book. ")
                print("Use the mkrec command to create a new recipe.")
                print("")
       

        elif command.startswith('rm'):
            # Distinguishes between similar starting inputs
            if command.startswith('rm -i'):
                # Removes ingredient from shopping list
                result = command[5:].split()
                ingredient_name = ''
                for i in result[:-1]:
                    # Checks if the element is a string
                    if type(i) == str:
                        # Add the string to ingredient_name with a space 
                        ingredient_name += i + ' '
                ingredient_name = ingredient_name.strip()
                # Converts the last element to a float and equals the amount
                amount = float(result[-1])
                generate_shopping_list(recipes)
                remove_from_shopping_list(ingredient_name, amount,
                shopping_list)
                shopping_list
            
            else:
                # Remove recipe from collection
                name = command[3:].strip()
                remove_recipe(name, recipes)
            
            
        elif command.lower() == 'ls':
            # Lists all recipes in the shopping cart
            if not recipes:
                print("No recipe in meal plan yet.")
            else:
                recipe_list = [recipe for recipe in recipes]
                print(recipe_list)


        elif command.lower() == 'ls -a':
            # Lists all recipes in recipe_collection
            for recipe in recipe_collection:
                print(recipe[0])

        elif command.lower() == 'ls -s':
            # Displays the shopping_list
            generate_shopping_list(recipes)
            if shopping_list!=[]:
                display_ingredients(shopping_list)
            else:
                pass    

        elif command.lower() == 'g' or command.lower() == 'G':
            # Generates a shopping_list
            shopping_list = generate_shopping_list(recipes)
            if shopping_list!=[]:
                display_ingredients(shopping_list)
            else:
                pass
        
        elif command.lower() == 'q' or command.lower() == 'Q':
            # Quits the loop and program
            break

        else:
            # Occurs when input doesn't match any statements
            print("Incorrect input, please try again")
        
if __name__ == "__main__":
    main()