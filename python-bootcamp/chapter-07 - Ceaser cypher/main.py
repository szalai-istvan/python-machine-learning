# Ceaser cypher
import ceasar
print("TYPE 'en [your text] [shift]' to encrypt")
print("TYPE 'de [your text] [shift]' to decrypt")
command = input('> ')
list = command.split(' ')

if len(list) < 3:
    print('Command length invalid: ' + list)
    exit()

method = list[0]

message = ''
for i in range(1, len(list) - 1):
    message = message + list[i] + ' '
message = message.upper()
shift = int(list[len(list) - 1])

result = ''
if list[0] == 'en':
    result = ceasar.encrypt(message, shift)
elif list[0] == 'de':
    result = ceasar.decrypt(message, shift)
else:
    print(f'Command identifier \'{list[0]}\' is invalid')
    exit()
print(f'{list[0]}crypted text is {result}')