InputArray = [0,1,1,0,1,0,0,0]
def myList(InputArray):
    b = len(InputArray) # length of input array
    MylistC = []        # array for Store occurrence 0.
    MyListD = []        # arr0y foe Store occurrence 1.
    for i in range (0, b):
        if InputArray[i]==0:
            MylistC.append(InputArray[i])

        if InputArray[i] == 1:
            MyListD.append(InputArray[i])
    FinalList = MylistC + MyListD
    return print(FinalList)
myList(InputArray)


