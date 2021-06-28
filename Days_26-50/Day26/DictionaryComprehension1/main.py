sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# word_list = [i for item in sentence for i in sentence.split()]
#word_list = sentence.split()
# Write your code below:
#{new_key:new_value for (key,value) in dictionary.items() if test}
result = {word:len(word) for word in sentence.split()}


print(result)

