import re
with open('Day4.txt') as file:
    sum = 0
    for row in file:
        row = row.replace('\n', '')
        row = row[9:].strip()
        parts = row.split('|')
        winning = re.split(r'\s{1,}', parts[0].strip())
        numbers = re.split(r'\s{1,}', parts[1].strip())

        score = 0.5
        for x in numbers:
            if x in winning:
                score *= 2
        if score == 0.5:
            score = 0
        sum += score
        print(f'I added {score} to sum, it is now {sum}')
        