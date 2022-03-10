from random import randint

# for numero in range(6):
#     print(numero)

#Return a number between 3 and 9 (both included):
# for numero in range(6):    
#     print(randint(1,60))


produtos = [
    ['p1', 128],
    ['p2', 430],
    ['p3', 318],
    ['p4', 785],
    ['p5', 855],
]
#print(sorted(produtos, key=lambda index: index[0]))
print(sorted(produtos, key=lambda index: index[0]))