

tmp = ""; arrOfLeft = []; arrOfRight = []
def run():
    global tmp; global arrOfLeft; global arrOfRight;
    tmp = [[['1', '2'], ['3', '4']], [['5', '6'],['7', '8']], [['9', '10'], ['11', '12']]]
    tmp = str(tmp)


    arrOfLeft = []
    arrOfLeft.append(0)
    # for x in range(0, len(tmp)):
    while(tmp[arrOfLeft[-1]]<=len(tmp)):
        print(x)

        arrOfLeft.append(tmp[arrOfLeft[-1]+2:len(tmp)].find('[[')+1 + arrOfLeft[-1])
        # x += arrOfLeft[-1]

    # for x in range(0, len(tmp)):
    arrOfRight=[]
    arrOfRight.append(0)
    while(tmp[arrOfRight[-1]]<=len(tmp)):
        
        arrOfRight.append(tmp[arrOfRight[-1]+2:len(tmp)].find(']]')+1 + arrOfRight[-1])



        # x+= arrOfRight[-1]



def runOLD():
    # tmp = [[['name?', 'sam'], ['time', 'noon'],['lucky', 'yup'] ], ['people', 'are awesome'], [['age', '12'], ['place', 'nowhere']]]

    tmp = [[['1', '2'], ['3', '4']], [['5', '6'],['7', '8']]]

    tmp=str(tmp)
    # while(tmp.find(']]')
    holdingArray = []
    pos = 0
    pos2 = 0
    while (pos2 < len(tmp)):
        # import pdb; pdb.set_trace()  # debugger

        pos = tmp[pos2:len(tmp)].find('[[') #0
        print('pos', pos)
        print('pos2', pos2)
        holdingArray.append(pos)



        # import pdb; pdb.set_trace() # debugger

        pos2 += tmp[pos:len(tmp)].find(']]') #23
        pos2 += 2                           #25
        holdingArray.append(pos2)

        pos += tmp[pos2:len(tmp)].find('[[') #27
        holdingArray.append(pos)            

        pos2 += tmp[pos+2:len(tmp)].find(']]') #end
        holdingArray.append(pos2)



        print('pos', pos)
        print('pos2', pos2)

        import pdb; pdb.set_trace() # debugger



        
        # pos2 = tmp[pos2+x:len(tmp)].find(']]')
        # x+=pos2

        
    print(holdingArray)

# index:
# start: 0, then +2
# end: 53+2
# start: 53+2+29: end
# end: 53+2+29+35+2

# [[ = 0
# ]] = 53
# new length = 29, on top of 53 and 2  -> 84 
# new length = 35, on top of 53, 2 and 29 -> 119