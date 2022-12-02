# Реализуйте алгоритм перемешивания списка.

import random
lst = [random.randint(0,11) for i in range(random.randint(0,15))]
print(f"исходный список:\n {lst}")
random.shuffle(lst)
print(f"список после перемешивания:\n{lst}")