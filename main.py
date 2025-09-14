### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, requied in ingredients.items():
            available = self.machine_resources.get(item , 0)
            if available < requied:
                print("Sorry there is not enough {item}.")
                return False
            return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins")
        def read_int(prompt):
            while True:
                try: 
                    val = input(prompt).strip()
                    if val == "":
                        return 0
                    n = int(val)
                    if n < 0: 
                        print("please enter a non-negative integer")
                        continue
                    return n
                except ValueError:
                    print("Please enter a whhole number (e.g., 0, 1, 2, ...).")
        
        dollars = read_int("how many large dollars?: ")
        halves = read_int("how many half dollars?: ")
        quarters = read_int("how many quarters?: ")
        nickels = read_int("how many nickels?: ")        

        total = dollars * 1.00 + halves * 0.50 + quarters * 0.25 + nickels * 0.05
        #return to the nearest cent to avoid floating point noise when printing
        return round(total + 1e-9, 2)
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost - 1e-9:
            print("Sorry that's not enough money. Money refunded.")
            return False
        change = round(coins - cost, 2)
        print(f"Here is ${change} in change")
        return True
    
           

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, required in order_ingredients.items():
            self.machine_resources[item] -= required
            print(f"{sandwich_size} sandwich is ready. Bon appetit.")

### Make an instance of SandwichMachine class and write the rest of the codes ###

def print_report(current_resources):
    print(f"Bread: {current_resources['bread']} slices")
    print(f"Ham: {current_resources['ham']} slices")
    print(f"Cheese: {current_resources['cheese']} ounces")
    
def main():
    machine = SandwichMachine(resources)
    VALID_SIZES = {"small", "medium", "large"}
    
    while True:
        choice = input("What would you like ? ( small/ medium/ large/ off/ report): ").strip().lower()
        
        if choice == "off":
            break
        elif choice == "report":
            print_report(machine.machine_resources)
        elif choice in VALID_SIZES:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]
            
            if not machine.check_resources(ingredients):
                continue
            inserted = machine.process_coins()
            
            if not machine.transaction_result(inserted, cost):
                continue
            machine.make_sandwich(choice, ingredients)
            
        else: 
            print("Invalid option. Please choose small, medium, large, report or off. ")
            
                
        