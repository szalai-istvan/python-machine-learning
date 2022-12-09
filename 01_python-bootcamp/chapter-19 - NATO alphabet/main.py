import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
dictionary = {row.letter:row.code for (index, row) in df.iterrows()}

def convert(character):
    if character.isalpha():
        return dictionary[character]
    return character

print('Input some text to translate to NATO phonetic alphabet! ')
text = input('> ').upper()
phonetic = [convert(letter) for letter in text]

print(phonetic)