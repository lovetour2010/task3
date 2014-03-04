class Animal(object):
    pass
	
## ?? is-a
class Dog(Animal):

    def __init__(self,name):
	    ##
	    self.name=name
		
## ?? is-a
class Cat(Animal):

    def __init__(self,name):
	    ## ?? has-a
	    self.name=name
		
## ?? has-a
class Person(object):

    def __init__(self,name):
	    ## ?? has-a
	    self.name=name
		
	    ## person has-a pet of some kind
	    self.pet=None
		
## ?? is-a
class Employee(Person):

    def __init__(self,name,salary):
	    ## ?? is-a hmm what is this strange magic?
	    super(Employee,self).__init__(name)
	    ## ?? has-a
	    self.salary=salary
		
## ?? has-a
class Fish(object):
    pass
	
## ?? is-a
class Salmon(Fish):
    pass
	
## ?? is-a
class Halibut(Fish):
    pass
	
## rover is-a Dog
rover=Dog("Rover")

## ?? is-a
satan=Cat("satan")

## ?? is-a
mary=Person("Mary")

## ??