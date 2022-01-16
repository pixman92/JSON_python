

def run():
    tmp = [[['name?', 'sam'], ['time', 'noon'],['lucky', 'yup'] ], ['people', 'are awesome'], [['age', '12'], ['place', 'nowhere']]]

    tmp=str(tmp)
    # while(tmp.find(']]')
    holdingArray = []
    for x in range (0, len(tmp)):
        pos = tmp[x:len(tmp)].find('[[')
        holdingArray.append(pos)
        pos2 = tmp[pos2+x:len(tmp)].find(']]')
        x+=pos2

        
    print(holdingArray)