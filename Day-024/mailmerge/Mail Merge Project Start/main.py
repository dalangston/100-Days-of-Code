#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


template = './Input/Letters/starting_letter.txt'
names_file = './Input/Names/invited_names.txt'
outdir = './Output/ReadyToSend'

name_list = []

with open(names_file) as names:
    with open(template) as letter:
        t_text = letter.read()

    for name in names:

        letter_text = t_text.replace('[name]', name.strip())

        with open(f'{outdir}/{name.strip()}.txt', 'w') as f:
            f.write(letter_text)
            
        
