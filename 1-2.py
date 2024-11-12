# Input string

L = False
F = False
R = False

input_string = '|*|-|\n|*|*|\n|-|-|\n|<|^>|\n'

rows = input_string.strip().split('\n')
result = []

for row in rows:
    columns = row.strip('|').split('|')
    result.append(columns)
transposed_result = list(zip(*result))
transposed_result = [list(row) for row in transposed_result]
for column in transposed_result:
    if column[2] == '*':
        if '<' in column[3]:
            L = True
        if '>' in column[3]:
            R = True
        if '^' in column[3]:
            F = True
    print(column)

res = ''
if L:
    res += 'L'
if F:
    res += 'F'
if R:
    res += 'R'

if not L and not F and not R:
    res = 'STOP'

print(res)

