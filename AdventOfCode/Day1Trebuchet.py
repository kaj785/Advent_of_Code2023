import os
print(os.getcwd())

numbers = ['0','1','2','3','4','5','6','7','8','9']
sum = 0
first_number = 0
last_number = 0
with open('trebuchet.txt') as file:
    for row in file:
        row = row.replace("\n", "")
        
        for x in range(0, len(row)):
            if row[x] in numbers:
                first_number = row[x]
                print(f'First number is {first_number}')
                x = 0
                break
        for y in range(-1, -(len(row)+1),-1):
            if row[y] in numbers:
                last_number = row[y]
                print(f'Second number is {last_number}')
                y = 0
                break
        whole_number = str(first_number) + str(last_number)
        print(f'Whole number in string form is {whole_number}')
        whole_number=int(whole_number)
        print(f'Converted to integer, whole number is {whole_number}')
        sum += whole_number
        print(f'adding it to sum, we have {sum}')
    print(sum)
