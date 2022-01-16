

def run():
    tmp = [[['name?', 'sam'], ['time', 'noon'],['lucky', 'yup'] ], ['people', 'are awesome'], [['age', '12'], ['place', 'nowhere']]]
    tmp = str(tmp)

    # while(tmp.find(']]')
    holdingArray = []
    for x in range (0, len(tmp)):
        holdingArray.append(tmp[x:len(tmp)].find('[['))

