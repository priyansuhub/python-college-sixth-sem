import numpy
myarray1=numpy.array([11,23,12,3,4,4,5,432,1], int)
myarray2=numpy.array(['a','b','c','d'])
myarray3=numpy.array(['lalala','udta hi firu', 'tu hai ke nahi hahahah'],dtype=str)
myarray4=numpy.array(['1.2','2.3'],float)
def testFunction():
    print(myarray1)
    print(myarray2)
    print(myarray3)
    print(myarray4)

testFunction()

my1 = myarray1.copy()
print(my1)
