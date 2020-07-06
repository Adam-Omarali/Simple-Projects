last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = list(zip(subjects, grades))

subjects.append("computer science")
grades.append(100)
gradebook.append(("visual arts", 93))

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)

#Excercise 2

toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)
print("We sell %d different kinds of pizza!" %num_pizzas)
pizzas = list(zip(prices, toppings))
pizzas.sort()
print(pizzas)
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
print(three_cheapest)
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
