import json
from flask import Flask, render_template, request

app = Flask(__name__)


# Function to load the recipes from the JSON file
def load_recipes():
    with open('food_recipes_main.json', 'r') as f:
        return json.load(f)

def load_recipes_dessert():
    with open('recipes.json', 'r') as f:
        return json.load(f)

# Function to filter recipes based on calorie and protein ranges
def filter_recipes(recipes, min_calories=None, max_calories=None, min_protein=None, max_protein=None):
    filtered_recipes = []

    for recipe in recipes:
        if min_calories and recipe['calories'] < min_calories:
            continue
        if max_calories and recipe['calories'] > max_calories:
            continue
        if min_protein and recipe['protein'] < min_protein:
            continue
        if max_protein and recipe['protein'] > max_protein:
            continue

        filtered_recipes.append(recipe)

    return filtered_recipes


@app.route('/')
def index():
    # Get filter parameters from the URL arguments
    min_calories = request.args.get('min_calories', type=int)
    max_calories = request.args.get('max_calories', type=int)
    min_protein = request.args.get('min_protein', type=int)
    max_protein = request.args.get('max_protein', type=int)

    recipes = load_recipes()  # Load all recipes from JSON

    # Filter recipes based on the query parameters
    filtered_recipes = filter_recipes(recipes, min_calories, max_calories, min_protein, max_protein)

    return render_template('index.html', recipes=filtered_recipes)


@app.route('/snacks')
def snacks():
    return render_template('snacks.html')


@app.route('/mains')
def mains():
    return render_template('mains.html')


@app.route('/desserts')
def desserts():
    # Get filter parameters from the URL arguments
    min_calories = request.args.get('min_calories', type=int)
    max_calories = request.args.get('max_calories', type=int)
    min_protein = request.args.get('min_protein', type=int)
    max_protein = request.args.get('max_protein', type=int)

    recipes = load_recipes_dessert()  # Load all recipes from JSON

    # Filter recipes based on the query parameters
    filtered_recipes = filter_recipes(recipes, min_calories, max_calories, min_protein, max_protein)

    return render_template('desserts.html', recipes=filtered_recipes)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
