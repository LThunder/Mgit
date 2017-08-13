#Filename: keyworld-only.py

def total(initial=5, *numbers, vegetables):
    count = initial
    for number in numbers: 
        count += number 
    count += vegetables
    return count

print(total(10, 1, 2, 3, vegetables=50))
print(total(10, 1, 2, 3))
#Raise error because wo have not supplied a default argument value for 'vegetables'