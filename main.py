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

def main_menu():
    db.init_db() # Make sure DB exists on startup

    while True:
        print("\n=== PANTRY PILOT MENU ===")
        print("1. Add Item to Pantry")
        print("2. Search for Recipes")
        print("3. View Inventory")
        print("4. Exit")

        choice = input("\nSelect an option (1-4): ")

        if choice == "1":
            name = input("Enter item name (e.g. Beef): ")
            qty = input("Enter quantity (e.g. 4 lbs): ")
            db.add_item(name, qty)
        elif choice == "2":
            run_recipe_search()
        elif choice == "3":
            items = db.get_inventory()
            print(f"\nIn your pantry: {', '.join(items) if items else 'Empty'}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again by choosing a number between 1-4.")

if __name__ == "__main__":
    main_menu()