#Fliename:while.py

number=20
running=True

while running:
  guess=int(input("Enter an integer:"))
   
  if guess==number:
    print("Congratulatiopn,you guessed it.")
    running=False #this cause the while loop to stop
  elif guess<number:
    print("No,it is a little higher.")
  else:
    print("No,it is a little lower.")
else:
  print("the while loop is over.")
  #Do anything else you want to do here

print("done")