


sum = 0
with open('Day2CubeConundrum.txt') as file:
    for row in file:
        add = True
        
        row = row.replace("\n", "")
        row = row.replace(";", ",")
        parts = row.split(': ')
        row = parts[1]
        
        cubes = row.split(',')
        
        for x in cubes:
            numberColour = x.strip().split(' ')[1]
            number = x.strip().split(' ')[0]

            if int(number) > 12 and numberColour == 'red':
                print(f'{number} for {numberColour} is too damn big')
                add = False
            elif int(number) > 13 and numberColour == 'green':
                print(f'{number} for {numberColour} is too damn big')
                add = False
            elif int(number) > 14:
                print(f'{number} for {numberColour} is too damn big')
                add = False
            

        if add:
            numbers = parts[0].split(' ')
            print(f'I will add {int(numbers[1])}')
            sum += int(numbers[1])
        
        
            print(f'I have added {numbers[1]}, the sum is now {sum}')
            

print('ANSWER BELOW')    
print(sum)

