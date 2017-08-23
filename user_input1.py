#Filename: user_input.py
import string

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    #return text == reverse(text)
    text = text.lower()
    text = text.replace(' ','')
    for char in string.punctuation:
        text = text.replace(char,'')
    return text == reverse(text)
#something = input('Enter text:')

#if (is_palindrome(something)):
#    print("Yes, it id a palindrome")
#else:
#    print("No, it is not palindrome")
def main():
    something = input('Enter text:')
    if (is_palindrome(something)):
        print('Yes, "{0}" is a palindrome'.format(something))
    else:
        print('No, "{0}" is not a palindrome'.format(something))

if __name__=='__main__':
    main()
else:
    print("user_inout.py was improted!")