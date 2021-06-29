#student_dict = {
#    "student": ["Angela", "James", "Liily"],#
#    "score": [56, 76, 98]
#}
#Looping through dictionaries:
#for (key,value) in student_dict.items():
    #print(value) or print(key)

#import pandas

#student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)
# for (key, value) in student_data_frame.items():
#     print(value)
#for (index,row) in student_data_frame.iterrows():
    # print(index)
#   print(row.student) # or print(row.score)

#{new_key:new_value for (index, row) in df.iterrows()}
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")
#{new_key:new_value for (key,value) in dictionary.items() if test}
dict = {row.letter:row.code for (index,row) in df.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Provide a word to spell it: ").upper()
#word_split = [char.capitalize() for char in word]
spell = [dict[letter] for letter in word]
print(spell)