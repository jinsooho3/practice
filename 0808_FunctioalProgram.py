def getInputValue(argNumOfInputValue):
    tempInputValueList = []
    for index in range(argNumOfInputValue):
        inputValue= input(str(index + 1) + "번째 입력 값: ")
        tempInputValueList.append(int(inputValue))
    return tempInputValueList

def myBubbleSort(argList, ascend = True):
    for iCount in range(len(argList)-1):
        for jCount in range(len(argList) - iCount - 1):
            comparisonResult = \
                argList[jCount] > argList[jCount + 1] if ascend else argList[jCount] < argList[jCount + 1]

            if comparisonResult:
                argList[jCount], argList[jCount + 1] = argList[jCount + 1] , argList[jCount]

inputValueList = getInputValue(5)

myBubbleSort(inputValueList, ascend = False)
print(inputValueList)