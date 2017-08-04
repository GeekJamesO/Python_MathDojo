# Assignment: MathDojo
# HINT: To do this exercise, you will probably have to use 'return self'.
# If the method returns itself (an instance of itself), we can chain methods.
#
# PART I
#     Create a Python class called MathDojo that has the methods add and subtract.
#     Have these 2 functions take at least 1 parameter.
#
#     Then create a new instance called md. It should be able to do the following task:
#
#     MathDojo().add(2).add(2, 5).subtract(3, 2).result
#     which should perform 0+2+(2+5)-(3+2) and return 4.
#
# PART II
#     Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter
#     with any number of values passed into the list.
#     It should now be able to perform the following tasks:
#        MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
#
#        should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.
#
# PART III
#     Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons.


class MathDojo:
    def __init__(self):
        self.result = 0;
        self.trace = True

    def add(self, *args):
        # aTouple = type( () )
        for count, aNumber in enumerate(args):
            if (isinstance(aNumber, int)):
                print( '  ADDInt:{0}. adding {1} to {2}'.format(count, self.result, aNumber))
                self.result += aNumber;
            elif (isinstance(aNumber, float)):
                print( '  ADDFlt:{0}. adding {1} to {2}'.format(count, self.result, aNumber))
                self.result += aNumber;
            elif (isinstance(aNumber, list)):
                tempMathDojo = MathDojo()
                for anEntry in aNumber :
                    tempMathDojo.add(anEntry) #RECURSION
                print( '  AddLIST:{0}. adding {1} to {2}'.format(count, self.result, tempMathDojo.result))
                self.result += tempMathDojo.result
            elif (isinstance(aNumber, type( () ) )):
                tempMathDojo = MathDojo()
                print " foo " , aNumber
                for aNumInTouple in aNumber:
                    tempMathDojo.add(aNumInTouple) #RECURSION
                print( '  AddTouple:{0}. adding {1} to {2}'.format(count, self.result, tempMathDojo.result))
                self.result += tempMathDojo.result
            else:
                print "this is of type", type(aNumber)
        return self

    def subtract(self, *args):
        for count, aNumber in enumerate(args):
            if (isinstance(aNumber, int)):
                print( '  SUBInt:{0}. subtracting {2} from {1}'.format(count, self.result, aNumber))
                self.result -= aNumber;
            elif (isinstance(aNumber, float)):
                print( '  SUBFlt:{0}. subtracting {2} from {1}'.format(count, self.result, aNumber))
                self.result -= aNumber;
            elif (isinstance(aNumber, list)):
                tempMathDojo = MathDojo()
                for anEntry in aNumber :
                    tempMathDojo.subtract(anEntry) #RECURSION
                print( '  SubLIST:{0}. subtracting {2} from {1}'.format(count, self.result, tempMathDojo.result))
                self.result += tempMathDojo.result  #you add values here.. is the already negated values.
            elif (isinstance(aNumber, type( () ) )):
                tempMathDojo = MathDojo()
                print " foo " , aNumber
                for aNumInTouple in aNumber:
                    tempMathDojo.add(aNumInTouple) #RECURSION
                print( '  SubTouple:{0}. subtracting {2} from {1}'.format(count, self.result, tempMathDojo.result))
                self.result += tempMathDojo.result
            else:
                print "this is of type", type(aNumber)
        return self

answer = MathDojo().add(2).add(2, 5).subtract(3, 2).result
print "result = ", answer

answer = MathDojo().add(3,[1,5,[11,12]]).result
print "result = ", answer

answer = MathDojo().add(8).subtract(1,2).result
print "result = ", answer
