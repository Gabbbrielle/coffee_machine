def make_coffee():
    from coffee_type import coffees
    from coffee_type import inventory

    latte = ['latte', 'Latte']
    espresso = ['espresso', 'expresso', 'espreso']
    cappuccino = ['cappuccino', 'capuccino', 'cappucino', 'cappuccinno']

    def user_choice():
        choice = input('What would you like? (espresso/latte/cappuccino): ')
        if choice in latte:
            return coffees[1]
        if choice in espresso:
            return coffees[0]
        if choice in cappuccino:
            return coffees[2]

    coffee_2_make = user_choice()
    accepted_coin = [.05, .10, .25]

    price = float(coffee_2_make['price'])
    total_in = 0
    paying = True

    while paying:
        if total_in < price:
            left_to_pay = price - total_in
            coin = float(input(f"{format(left_to_pay, '.2f')}$, Insert a coin: .25\xa2, .10\xa2 or .05\xa2.: "))
            if coin not in accepted_coin:
                print('(money returned) Only coins accepted are: .25\xa2, .10\xa2 or .05\xa2.')
            else:
                total_in = total_in + coin
        elif total_in > price:
            print(f"{format(total_in - price, '.2f')}$ is your change. Enjoy your coffee")
            paying = False
            inventory['profit'] += price
            inventory["water"] -= coffee_2_make["water"]
            inventory["coffee"] -= coffee_2_make["coffee"]
            inventory["milk"] -= coffee_2_make["milk"]
        elif total_in == price:
            print("Enjoy your coffee")
            paying = False
            inventory['profit'] += price
            inventory["water"] -= coffee_2_make["water"]
            inventory["coffee"] -= coffee_2_make["coffee"]
            inventory["milk"] -= coffee_2_make["milk"]
            print(inventory)
            make_coffee()

make_coffee()
