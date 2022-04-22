PLACEHOLDER = '[name]'

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

for line in names:
    final_letter = letter.replace(PLACEHOLDER, line.strip())
    with open(f"./Output/ReadyToSend/{line.strip()}.txt","w") as completed_letter:
        completed_letter.write(final_letter)
        