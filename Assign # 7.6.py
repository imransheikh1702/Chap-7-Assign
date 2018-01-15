prompt = "\nPlease enter your favourite toppings: "
prompt += "\nEnter quit when you finished. "

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
print (available_toppings)

requested_toppings = []

while True:
    top = input(prompt)
    requested_toppings.append(top)
    if top == 'quit':
        del requested_toppings[-1]
        print("Your selected toppings: ")
        print(requested_toppings)
        break
    else:
        print("\nYou add " + top.title() + " topping to the pizza.")