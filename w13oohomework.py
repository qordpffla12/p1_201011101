class Dog(object):
    def bark(self):
        print "mung mung"
class Sichew(Dog):
    def bark(self):
        print "si si"
class Martis(Dog):
    def bark(self):
        print "mal mal"

dogOne = Dog()
dogTwo = Sichew()
dogThree = Martis()
dogOne.bark()
dogTwo.bark()
dogThree.bark()