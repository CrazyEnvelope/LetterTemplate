with open("Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

with open("Input/Names/invited_names.txt") as names:
        for name in names:
                name = name.replace("\n","")
                with open(f"Output/ReadyToSend/letter_to_{name}.txt", mode="w") as letter_to_send:
                    letter_to_send.write(letter_content.replace("[name]",name))



