#Filename: using_file.py

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use python
'''

f = open('poem.text','w') #open for 'w'riting
f.write(poem) #write text to file
f.close() #close the file

f = open('poem.text') #if no mode is specified, 'r'ead mode is assumed by default

while True:
    line = f.readline()
    if len(line) == 0:#zero lenth indicater EOF
        break
    print(line, end='')
f.close() #close the file