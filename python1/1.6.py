import random
my_tuple = [random.randint(0, 100) for i in range(10)]
print("tuple - ", my_tuple, "\nmax - ",max(my_tuple), " min - ", min(my_tuple))