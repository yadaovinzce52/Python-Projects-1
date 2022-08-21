import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row['letter']: row['code'] for (index, row) in nato_data.iterrows()}
print(nato_dict)


def generate_phonetic():
    input_string = input('Enter a word: ').upper()
    try:
        list_phonetic = [nato_dict[letter] for letter in input_string]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()
    else:
        print(list_phonetic)


generate_phonetic()
