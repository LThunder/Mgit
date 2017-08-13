#Filename: func-total.py

def total(initial=5, *numbers, **keyworlds):
    count = initial
    for number in numbers:
        count += number
    for key in keyworlds:
        count += keyworlds[key]
    return count

print(total(10, 1, 2, 3, vegetable=50, fruits=100))