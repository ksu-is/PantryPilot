import requests

# Use your API Key from Spoonacular API
API_KEY = "78835df1b4564ff6b0dc65fcc105d473"

def find_recipes(ingredients):
    url = "https://api.spoonacular.com/recipes/findByIngredients"

    # Parameters to send to the API
    query_params = {
        "ingredients": ",".join(ingredients),
        "number": 3, # We only want the top 3 results
        "apiKey": API_KEY
    }

response = requests.get(url, params=query_params)

# If the response is successful (200 OK)
if response.status_code == 200:
    return response.json()
else:
    print("Error connecting to the API.")
    return []