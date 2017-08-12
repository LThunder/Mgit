#Fliename

while True:
    s=input('Enter something:')
    if s=='quit':
        break 
    if len(s)<3:        
        print('Too small')
    elif len(s)>5:
        print('Too big')
    continue
    print('Input is of sufficient length')
    #Do other kinds of processing here...