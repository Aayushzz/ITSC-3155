import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()



def main():
    ###  write the rest of the codes ###
    print("Welcome to the Sandwich Maker Machine!")
    while True:
        choice = input("What would you like? (small/medium/large) or 'report' or 'off': ").strip().lower()

        if choice == "off":
            print("Turning off. Goodbye!")
            break

        if choice == "report":
            print("Resources report:")
            print(f"Bread:  {resources['bread']} slice(s)")
            print(f"Ham:    {resources['ham']} slice(s)")
            print(f"Cheese: {resources['cheese']} ounce(s)")
            continue

        if choice not in recipes:
            print("Invalid option. Please choose 'small', 'medium', or 'large'.")
            continue
        
        recipe = recipes[choice]
        needed = recipe["ingredients"]
        cost = recipe["cost"]
        
        if not sandwich_maker_instance.check_resources(needed):
            continue
        
        print(f"The {choice} sandwich costs ${cost:.2f}. Please insert coins.")
        inserted = cashier_instance.process_coins()
        if not cashier_instance.transaction_result(inserted, cost):
            continue
        
        sandwich_maker_instance.make_sandwich(choice, needed)

if __name__=="__main__":
    main()