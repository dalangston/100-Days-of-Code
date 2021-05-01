import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
alphabet_df = pandas.read_csv('./nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index,row) in alphabet_df.iterrows()}
#print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word >  ").upper()
codes = [nato_dict[l] for l in word]
print(codes)