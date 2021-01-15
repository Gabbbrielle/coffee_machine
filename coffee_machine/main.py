def make_coffee():
    from coffee_type import coffees
    from coffee_type import inventory
    import os
    def clear(): os.system('cls')

# allow for spelling mistake from the user.
    coffee_type = ['latte', 'espresso', 'cappuccino']
    latte = ['latte', 'Latte']
    espresso = ['espresso', 'expresso', 'espreso']
    cappuccino = ['cappuccino', 'capuccino', 'cappucino', 'cappuccinno']

    def check_inventory():
        name = []
        for key in coffees:
            name.append(key['name'])
        # used to print the list of names available to clients
        coffee_choices = name
        # print to validate the coffee_type works
        # checks for ressource in inventory and will remove the choice that can't be done anymore
        for item in coffees:

            if inventory['water'] < item['water']:
                coffee_choices.remove(item['name'])
                print(f"{item['name']} (not available)")

            if inventory['coffee'] < item['coffee']:
                coffee_choices.remove(item['name'])
                print(f"{item['name']} (not available)")

            if inventory['milk'] < item['milk']:
                coffee_choices.remove(item['name'])
                print(f"{item['name']} (not available)")

        return ', '.join(coffee_choices)

    choices = check_inventory()

    def user_choice():
       
        """Return the dictionary of the coffee chosen with qty for price, water, coffee and milk """
        choice = input(f'What would you like? {choices}: ')
        if choice in latte:
            return coffees[1]
        elif choice in espresso:
            return coffees[0]
        elif choice in cappuccino:
            return coffees[2]
        elif choice == 'report' or choice == 'off':
            if choice == 'report':
                report()
            elif choice == 'off':
                clear()
                print("coffee machine off")
            turn_on = input("Type 'on' to resume machine operations: ")
            if turn_on == "on":
                make_coffee()
            else:
                clear()
                print('\nwrong command. You just broke the machine.\nPlease call tech support ')
                exit(code='code 13')
        else:
            print('wrong choice, try again')
            make_coffee()

    def report():
        """print the inventory (profit, water, coffee, milk) formatted"""
        for key, value in inventory.items():
            print(str(key) + ': ' + str(value))


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
            make_coffee()


make_coffee()
