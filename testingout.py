

def run():
    # tmp = [[['name?', 'sam'], ['time', 'noon'],['lucky', 'yup'] ], ['people', 'are awesome'], [['age', '12'], ['place', 'nowhere']]]

    tmp = [[['1', '2'], ['3', '4']], [['5', '6'],['7', '8']]]

    tmp=str(tmp)
    # while(tmp.find(']]')
    holdingArray = []
    pos = 0
    pos2 = 0
    while (pos2 < len(tmp)):
        # import pdb; pdb.set_trace()  # debugger

        pos = tmp[pos2:len(tmp)].find('[[')
        print('pos', pos)
        print('pos2', pos2)
        holdingArray.append(pos)



        # import pdb; pdb.set_trace() # debugger

        pos2 = tmp[pos:len(tmp)].find(']]') 
        pos2 += 2 
        holdingArray.append(pos2)

        pos = tmp[pos2:len(tmp)].find('[[')



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