class MathDojo(object):
    """docstring for MathDojo."""
    def __init__(self):
        self.result = 0

    def add(self, *args):
        if None == args:
            pass
        else:
            for arg in args:
                if None == arg:
                    pass
                elif isinstance(arg, int):
                    self.result += arg
                elif isinstance(arg, float):
                    self.result += arg
                elif isinstance(arg, list):
                    for index in range(0,len(arg)):
                        self.add(arg[index])
                elif isinstance(arg, tuple):
                    for index in range(0,len(arg)):
                        self.add(arg[index])
                else:
                    print "Type for this is ", type(arg)
                    print "What is the type of this monster?'{}' ?".format(arg)
        return self

    def subtract(self, *args):
        if None == args:
            pass
        else:
            for arg in args:
                if None == arg:
                    pass
                elif isinstance(arg, int):
                    self.result -= arg
                elif isinstance(arg, float):
                    self.result -= arg
                elif isinstance(arg, list):
                    for index in range(0,len(arg)):
                        self.subtract(arg[index])
                elif isinstance(arg, tuple):
                    for index in range(0,len(arg)):
                        self.subtract(arg[index])
                else:
                    print "Type for this is unknown: ", type(arg)
                    print "What is the type of this monster?'{}' ?".format(arg)
        return self

    def testCases(self):
        print "Integers"
        print "  add(None)            Expect  0:", md.add(None).result
        print "  add(1)               Expect  1:", md.add(1).result
        print "  add(1)               Expect  2:", md.add(1).result
        print "  add(1, 2)            Expect  5:", md.add(1, 2).result
        md.result = 0

        print "  subtract(None)       Expect  0:", md.subtract(None).result
        print "  subtract(1)          Expect -1:", md.subtract(1).result
        print "  subtract(1, 2)       Expect -4:", md.subtract(1, 2).result
        print "  subtract(-1, 0)      Expect -3:", md.subtract(-1, 0).result
        print "  subtract(-1, -2)     Expect  0:", md.subtract(-1, -2).result
        md.result = 0
        print " "

        print "Lists"
        print "  add([])        Expect  0:", md.add([]).result
        print "  add([3])       Expect  3:", md.add([3]).result
        print "  add([-1,5])     Expect 7:", md.add([-1,5]).result
        md.result = 0

        print "  subtract([])        Expect  0:", md.subtract([]).result
        print "  subtract([3])       Expect -3:", md.subtract([3]).result
        print "  subtract([3,5])     Expect -11:", md.subtract([3,5]).result
        md.result = 0

        print "Lists within Lists"
        print "  add([[1,3],5]) Expect  9:", md.add([[1,3],5]).result
        print "  subtract([3,5],[1,7]) Expect -7", md.subtract([3,5],[1,7]).result
        print " "
        md.result = 0

        print "Touples"
        print "  add( ( ) )     Expect  0:", md.add( ( ) ).result
        print "  add((7))       Expect  7:", md.add( (7) ).result
        print "  add((1,3))     Expect  11:", md.add( (1,3) ).result
        print "  add((1,3,5))   Expect  20:", md.add( (1,3,5) ).result
        print "  subtract( ( ) )     Expect  20:", md.subtract( ( ) ).result
        print "  subtract((7))       Expect  13:", md.subtract( (7) ).result
        print "  subtract((1,3))     Expect  9:", md.subtract( (1,3) ).result
        print "  subtract((1,3,5))   Expect  0:", md.subtract( (1,3,5) ).result
        md.result = 0
        #
        print "Touples that contain Touples"
        print "  add(((1,3),5)) Expect  9:", md.add(((1,3),5)).result
        print "  subtract(((1,3),5)) Expect  0:", md.subtract(((1,3),5)).result
        md.result = 0
        print " "

        print "Integers with Lists that contain lists and Touples in Touples, and List that have touples and touples that have Lists..  Are you crazy?"
        print "  add(1,[3, (5,(7,[9,11])) , [13,17] ])  Expect 66:", md.add(1,[3, (5,(7,[9,11])) , [13,17] ]).result

md = MathDojo()
# md.testCases()
md.result = 0
print "  md.add(2).add(2,5).subtract(3,2)   Expect 4:", md.add(2).add(2,5).subtract(3,2).result
md.result = 0
print "  md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result:  Expect 28.15:", md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
