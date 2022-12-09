# Basic calculator
import operations

signs = {
    '+': operations.add,
    '-': operations.substract,
    '*': operations.multiply,
    '/': operations.divide
}

print('Give two numbers with an operation sign, separated by space characters')
command = input('> ')
parts = command.split(' ')
if len(parts) != 3:
    print(f'invalid command {command}')
    exit(0)

if not parts[0].isnumeric():
    print(f'Error converting {parts[0]} to a number')
    exit(0)

if not parts[2].isnumeric():
    print(f'Error converting {parts[2]} to a number')
    exit(0)

n1 = float(parts[0])
op = parts[1]
n2 = float(parts[2])

if not signs.__contains__(op):
    print(f'Invalid operand "{op}"')
    exit(0)

function = signs[op]
result = function(n1, n2)

print(f'{command} = {result}')