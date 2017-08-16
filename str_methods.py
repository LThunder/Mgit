#Filename: str_methods.py

name = 'Swaroop' # This is a string object

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "a"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'india', 'china']
print(delimiter.join(mylist))