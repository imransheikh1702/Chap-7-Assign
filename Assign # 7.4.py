prompt = "\nPlease enter your favourite toppings: "
prompt += "\nEnter quit when you finished. "

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
print (available_toppings)

requested_toppings = []

active = True
while active:
    top = input(prompt)
    requested_toppings.append(top)
    if top == 'quit':
        active = False
        del requested_toppings[-1]
        print("Your selected toppings: ")
        print(requested_toppings)
    else:
        print("I'll add " + top.title() + " topping to the pizza.")