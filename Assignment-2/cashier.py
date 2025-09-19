class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        try: 
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickels = int(input("how many mickels?: "))
            pennies = int(input("how manu pennies?: "))
        except ValueError:
            print("Invalid input detected. Treating non-numeric entries as 0.")
            quarters = dimes = nickels = pennies = 0
        
        total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
        return round(total, 2)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry that's not enough money, Money refunded")
            return False
        change = round(coins - cost, 2)
        if change > 0: 
            print(f"Here is ${change} in change")
        return True