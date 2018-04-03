
class Dog():

    def __init__(self, name='Silvio', age=5, breed=None):
        self.name = name
        self.age = age
        self.breed = breed


    def intro(self):
        print("Hello, my name is {} and I am {} years old. BTW I am a dog.".format(self.name, self.age))

    def walk(self):
        print("Dog named {} is walking.".format(self.name))


class Desidog(Dog):

    def __init__(self, name, age, breed=None):

        super().__init__(name, age, breed)

    def walk(self):
        print("desi dog named {} is walking".format(self.name))


d = Desidog("sheru", 15)
d.walk()

if d.breed:
    print("breed of {} is: {}".format(d.name, d.breed))
else:
    print("no breed assigned to dog: {}".format(d.name))