inputArray = [2,3,6,7]
def mySum(inputArray):
    b = len(inputArray)     # length of input array .
    myVar = 0               # variable to store sum .
    for i in range (0, b):
        myVar = myVar + inputArray[i]
    return print(myVar)
mySum(inputArray)
