# 키보드로 부터 N개의 정수를 입력 받아 리스트에 저장
def getInputValue(argNumOfInputValue):
    tempInputValueList = []
    for index in range(argNumOfInputValue):
        inputValue = input(str(index + 1) + "번째 입력 값: ")
        tempInputValueList.append(int(inputValue))
    return tempInputValueList

# 리스트에 저장된 정수 값을 오름 차순으로 저장
def myBubbleSort(argList):
    for iCount in range(len(argList) - 1):
        for jCount in range(len(argList) - iCount - 1):
            if argList[jCount] > argList[jCount + 1]:
                argList[jCount], argList[jCount + 1] = argList[jCount + 1] ,argList[jCount]
                # temp = argList[jCount]
                # argList[jCount] = argList[jCount + 1]
                # argList[jCount + 1] = temp


inputValueList = getInputValue(5)

myBubbleSort(inputValueList)
print(inputValueList)