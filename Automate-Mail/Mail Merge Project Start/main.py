# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Names/invited_names.txt', mode='r') as names:
    name_list = names.readlines()

with open('./Input/Letters/starting_letter.txt', mode='r') as letter:
    contents = letter.read()
    for name in name_list:
        name = name.strip('\n')
        with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as letter_to_write:
            new_letter = contents.replace('[name]', name)
            letter_to_write.write(new_letter)
