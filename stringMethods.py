'''Methods are functions that belong to an object. Example of string methods
are title(), islower(), count(), capitilize() ,format(), split() and many more'''

#Title Method
name = "abrefi matilda"
print(name.title())

#Format Method
location = "payin anim st. " 
print(location.format())

#Count Method
Animals = "fish, birds, lion, tiger,fish"
print(Animals.count('fish'))

#print(3.5.islower)

#Split method
new_str = "The cow jumped over the moon."
print(new_str.split())
print(new_str.split(' ', 3))
print(new_str.split('.'))
print(new_str.split(None, 3))

#Quiz 1: String Methods Coding Practice
'''Below, we have a string variable that contains the first verse of the poem, If by Rudyard Kipling(opens in a new tab). Remember, \n is a special sequence of characters that causes a line break (a new line).Use the code editor below to answer the following questions about verse and use Test Run to check your output in the quiz at the bottom of this page.

What is the length of the string variable verse?
What is the index of the first occurrence of the word 'and' in verse?
What is the index of the last occurrence of the word 'you' in verse?
What is the count of occurrences of the word 'you' in the verse?
You will need to refer to Python's string methods documentation(opens in a new tab).'''

#solution
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)
print(len(verse))
print(verse.index("and"))
print(verse.index("you",150))
print(verse.count("you"))
# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!