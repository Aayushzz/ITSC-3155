
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, required in ingredients.items():
            available = self.machine_resources.get(item, 0)
            if available < required:
                print(f"Sorry, there is not enough {item}. Need {required}, have{available}")
                return False
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item , amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"Here is you {sandwich_size} sandwich. Enjoy!")
        
        