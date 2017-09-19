from random import *

print("randint result : ", randint(1, 100))
print("uniform result : ", uniform(1, 100))

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("original items : ", items)
shuffle(items)
print("shuffle result : ", items)

items_name = ['Alissa','Alice','Marco','Melissa','Sandra','Steve']
print("sample1 result  : ", sample(items_name,  1))    # Pick a random item from the list
print("sample2 result  : ", sample(items_name,  2))    # Pick a random item from the list

