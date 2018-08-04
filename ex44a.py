class Parent(object):
    def implicit(self):
        print "PARAENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
