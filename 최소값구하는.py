minimum = None
print('Before:',minimum)
for itervar in [3, 41, 12, 9, 74, 15]:
    if minimum is None or itervar < minimum :
        minimum = itervar
    print('Loop:', itervar, minimum)
print('Minimum:', minimum)
