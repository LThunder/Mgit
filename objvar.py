#Filename: obivar.py

class Robot:
    '''Represrnts a robot, with a name.'''

    #A class variable, counting the number of robots
    population = 0

    def __init__(self,name):
        '''Initialize the data.'''
        self,name = name 
        print('(Initialize {0})'.format(self.name)

        #When this person is created, the robot
        # adds to the population 
        Robot.population += 1

    def __del__(self):
        '''I am dying.'''
        print('{0} is being destoroyed!'.format(self.name))

        Robot.popution -= 1

        if Robot.population == 0:
            print('{0} was the last one.'.format(self.name))
        else:
        print('There are still {0:d} robots working.'.format(Robot.population))

    def sayHi(self):
        '''Greeting by the robot.

        Yeah, they can do the.'''
        print('Greetings, my master call me {0}.'.format(self.name))

    def howMany()
        '''Print the current popution.'''
        print('We have {0:d} robots.'.format(Robot.population)
    howMany = staticmethod(howMany)

droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3P0')
droid2.sayHi()
Robot.howMany()

print("\nRobots can do some work here.\n")

print("Robos have finished their work. So let's destroy them.")

del drois1
del droid2
robot.howMany()