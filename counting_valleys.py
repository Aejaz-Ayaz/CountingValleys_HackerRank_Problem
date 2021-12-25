hike = 'UDDUUDDU'

dict1 = {'D':-1, 'U':1}

sealevel = 0

downstep = 0

valley_complete = 0

for i in hike:
    sealevel += dict1[i]

    if sealevel < 0 and i == 'D':
        downstep -= 1

    elif sealevel <= 0 and i == 'U':
        downstep += 1
        if downstep == 0:
            valley_complete += 1
    else:
        pass

print(valley_complete)
