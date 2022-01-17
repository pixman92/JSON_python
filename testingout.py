

tmp = ""; arrOfLeft = []; arrOfRight = []
def run():
    global tmp; global arrOfLeft; global arrOfRight;
    tmp = [[['13', '14']], [['1', '2'], ['3', '4']], [['5', '6'],['7', '8']], [['9', '10'], ['11', '12']]]
    tmp = str(tmp)

    # for x in range(0, len(tmp)):
    # while(arrOfLeft[-1]<=len(tmp)):
        # print(x) 
    arrOfLeft = []
    arrOfLeft.append(0)
    # for x in range(0, len(tmp)):
    arrOfRight=[]
    arrOfRight.append(0)

    if(tmp[0:len(tmp)].find('[[[')==0):
        arrOfLeft[0] = 2

    while(arrOfRight[-1]+4<len(tmp)):
        arrOfLeft.append(tmp[arrOfLeft[-1]+2:len(tmp)].find('[[') + arrOfLeft[-1] +1)

        arrOfRight.append(tmp[arrOfRight[-1]+2:len(tmp)].find(']]')+ arrOfRight[-1] +1)

    reduce()
    printArrs()


def reduce():
    # left UP by 2
    for x in range(1, len(arrOfLeft)):
        arrOfLeft[x] += 2

    for x in range(1, len(arrOfRight)):
        arrOfRight[x] += 2
    # printArrs()    


def printArrs():
    print ("===")
    print ('left: [[: ', arrOfLeft)
    print ("===")
    print ('right: "]]: ', arrOfRight)
    # for x in range(1, len(arrOfRight)):
        # arrOfRight[x] -=1s

arrayPulled=[]
def pullIndexesOfBetweenBrackets():
    global arrayPulled
    for x in range (0, len(arrOfLeft)):
        if(x<len(arrOfRight)):  
            arrayPulled.append(tmp[arrOfLeft[x]:arrOfRight[x+1]])
        else:
            arrayPulled.append(tmp[arrOfLeft[x]:arrOfRight[x]])

        



