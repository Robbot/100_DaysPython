PLACEHOLDER = "[name],"

with open("./Input/Names/invited_names.txt") as f:
    names = f.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    content = file.read()
    for name in names:
        new_letter = content.replace(PLACEHOLDER, name)
        stripped_name = name.strip()
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)