



with open('GearRatioDay3Input.txt') as file:
    sum = 0
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    indexing = []
    '''for y in range (0,140):
        indexing.append([])'''
    number_of_lines = 0
    for y in file:
        y = y.replace('\n', '')
        indexing.append([])
        for x in y:
            indexing[number_of_lines] += x
        number_of_lines += 1
        rowlength = len(y)
    print('number of lines:')
    print(number_of_lines)
    print('length of row')
    print(rowlength)

    print('the first row, 26th element is:')
    print(indexing[0][25])
    
    for y in range(0,140):
        x = 0
        while x < 140:
            number = ''
            if indexing[y][x] in numbers:
                lowerlimit = [y,x]
                
                number += indexing[y][x]
                x += 1
                while x < 140 and indexing[y][x] in numbers:
                    
                    number += indexing[y][x]
                    x += 1
                upperlimit = [y,x-1]
                print('number found!', number)
                print(f'index at x = {lowerlimit[1]} to {upperlimit[1]}, y at {lowerlimit[0]}')
                add = False
                if lowerlimit[0] > 0:
                    for z in range(lowerlimit[1],upperlimit[1]+1):
                        print(f'{indexing[lowerlimit[0]-1][z]} is from {lowerlimit[0]-1},{z}')
                        if indexing[lowerlimit[0]-1][z] != '.' and indexing[lowerlimit[0]-1][z] not in numbers:
                            add = True
                        
                if lowerlimit[0] < 139:
                    for z in range(lowerlimit[1],upperlimit[1]+1):
                        if indexing[lowerlimit[0]+1][z] != '.' and indexing[lowerlimit[0]+1][z] not in numbers:
                            add = True

                if lowerlimit[1] > 0:
                    if lowerlimit[0] != 0 and lowerlimit[0] != 139:
                        for z in range(lowerlimit[0]-1, lowerlimit[0]+2):
                            if indexing[z][lowerlimit[1]-1] != '.' and indexing[z][lowerlimit[1]-1] not in numbers:
                                add = True
                    if lowerlimit[0] == 139:
                        for z in range(lowerlimit[0]-1, lowerlimit[0]+1):
                            if indexing[z][lowerlimit[1]-1] != '.' and indexing[z][lowerlimit[1]-1] not in numbers:
                                add = True
                    if lowerlimit[0] == 0:
                        for z in range(lowerlimit[0], lowerlimit[0]+2):
                            if indexing[z][lowerlimit[1]-1] != '.' and indexing[z][lowerlimit[1]-1] not in numbers:
                                add = True


                
                if upperlimit[1] < 139:
                    if lowerlimit[0] != 0 and lowerlimit[0] != 139:
                        for z in range(lowerlimit[0]-1, lowerlimit[0]+2):
                            if indexing[z][upperlimit[1]+1] != '.' and indexing[z][upperlimit[1]+1] not in numbers:
                                add = True
                    if lowerlimit[0] == 139:
                        for z in range(lowerlimit[0]-1, lowerlimit[0]+1):
                            if indexing[z][upperlimit[1]+1] != '.' and indexing[z][upperlimit[1]+1] not in numbers:
                                add = True
                    if lowerlimit[0] == 0:
                        for z in range(lowerlimit[0], lowerlimit[0]+2):
                            if indexing[z][upperlimit[1]+1] != '.' and indexing[z][upperlimit[1]+1] not in numbers:
                                add = True
                if add:
                    print(f'added {number}')
                    sum += int(number)
                    print(f'the sum is now {sum}' )
                else:
                    print(f'the number {number} was not added')

            if x < 140:
                x += 1
    print(f'final sum is {sum}')
                

