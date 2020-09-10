import unittest

def classifyTriangle(a, b, c ):
    
    if a ==  b == c:
        print("Equilateral Triangle")
        if a**2 + b**2 == c**2 | a**2 + c**2 == b**2 | b**2 + c**2 == a**2:
            print("Right Triangle")
    elif a == b != c | a != b == c | a == c !=b:
        print("Scalene Triangle")
        if a**2 + b**2 == c**2 | a**2 + c**2 == b**2 | b**2 + c**2 == a**2:
            print("Right Triangle")
    elif a != b != c:
        print("Isosceles Triangle")
        if a**2 + b**2 == c**2 | a**2 + c**2 == b**2 | b**2 + c**2 == a**2:
            print("Right Triangle") 

def runClassifyTriangle(a, b, c):
    classifyTriangle(a,b,c)

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classifyTriangle(10,15,30),'Scalene','Should be Isoceles')




if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    
    #unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=True)  # this runs all of the tests - use this line if running from the command line
    