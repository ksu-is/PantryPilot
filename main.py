import database_manager as db
import spoonacular_client as api

def run_recipe_search():
    # 1. Get list of ingredients from SQLite DB
    pantry_items = db.get_inventory()

    if not pantry_items:
        print("\n[!] Your pantry is empty. Add some items first!")
        return
    
    print(f"\n[?] Searching recipes using: {', '.join(pantry_items)}...")

    # 2. Pass items to API client
    results = api.find_recipes(pantry_items)

    # 3. Display the results to the user
    if results:
        print("\n--- SUGGESTED RECIPES ---")
        for recipe in results:
            print(f"-> {recipe['title']} (Uses {recipe['usedIngredientCount']} of your items)")
    else:
        print("\n[!] No recipes found or API error occurred.")

    # Test it once!
if __name__ == "__main__":
    db.init_db()
    run_recipe_search()