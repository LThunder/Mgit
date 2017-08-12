#Fliename:if.py

number=23
guess=int(input('Enter an integer:'))

if guess==number:
  print('Congratulatins,you guessed it.')#New block starts here
  print('(but you do not win any prizes!)')#New block ends here
elif guess<number:
  print('No,it is a little higher than that')
  #You can do whatever you want in a block...
else:
    print('No,it is a little lower then that')
    #you must have guess >number to reach here
print('Done')
#This last statement is always esecuted,after the if statement is exected