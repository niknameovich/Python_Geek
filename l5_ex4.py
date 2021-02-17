translation = {'One': 'Литр', 'Two': 'Поллитра', 'Three': 'Банка', 'Four': 'Стакан'}

with open('exercise3.txt', 'r', encoding='utf-8') as source:
    with open('exercise4_translated.txt', 'w', encoding='utf-8') as target:
        for line in map(lambda x: x.split(), source):
            target.write(f'{translation[line[0]]} {line[-1]}\n')

print(list(open('exercise4_translated.txt', 'r', encoding='utf-8')))
