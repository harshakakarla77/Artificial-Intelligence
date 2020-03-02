import random

class Environment(object):
    def __init__(self):
        self.locationCondition = {'A': '0', 'B': '0'}
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)

class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        print(Environment.locationCondition)
        Score = 0
        vacuumLocation = random.randint(0, 1)
        if vacuumLocation == 0:
            print("Vacuum is randomly placed at location A")
            if Environment.locationCondition['A'] == 1:
                print("Location A is dirty")
                Environment.locationCondition['A'] = 0
                Score += 1
                print("Location A has been cleaned")

                if Environment.locationCondition['B'] == 1:
                    print("Location B is Dirty.")
                    print("Moving to location B")
                    Score -= 1 
                    Environment.locationCondition['B'] = 0
                    Score += 1
                    print("Location B has been cleaned")
            else:

                if Environment.locationCondition['B'] == 1:
                    print("Location B is dirty")
                    Score -= 1
                    print("Moving to Location B")
                    Environment.locationCondition['B'] = 0
                    Score += 1
                    print("Location B has been cleaned")

        elif vacuumLocation == 1:
            print("Vacuum is randomly placed at location B")
            if Environment.locationCondition['B'] == 1:
                print("Location B is dirty")
                Environment.locationCondition['B'] = 0;
                Score += 1
                print("Location B has been cleaned")

                if Environment.locationCondition['A'] == 1:
                    print("Location A is dirty")
                    Score -= 1
                    print("Moving to location A")
                    Environment.locationCondition['A'] = 0;
                    Score += 1
                    print("Location A has been cleaned")
            else:
                if Environment.locationCondition['A'] == 1:
                    print("Location A is dirty")
                    print("Moving to location A")
                    Score -= 1
                    Environment.locationCondition['A'] = 0;
                    Score += 1
                    print("Location A has been cleaned")
        print(Environment.locationCondition)
        print("Performance Measurement: " + str(Score))

theEnvironment = Environment()
theVacuum = SimpleReflexVacuumAgent(theEnvironment)
