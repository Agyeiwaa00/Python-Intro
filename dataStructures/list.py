list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[2])
print(list_of_random_things[1])
print(list_of_random_things[len(list_of_random_things) - 1] )

# List slicing
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
p3 = months[6:9]
print(p3)

first_half = months[:6]
print(first_half)

second_half = months[6:]
print(second_half)

greeting = "Hello there"
print(len(greeting), len(months))

# Are you in or not in
print ('this' in 'this is a string')
print('in' in 'this is a string')
print('isa' in 'this is a string')
print(5 not in [1, 2, 3, 4, 6])
print (5 in [1, 2, 3, 4, 6])

# Mutability : Ability to change order of object
# List is mutable data type  but string immutable
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)

'''greeting = "hello world"
greeting[0] ="M"
print(greeting)'''

# quiz
sentence1 = "I wish to register a complaint."
sentence2 = sentence1.split()
print(sentence2)
# sentence2[6] ="!" # this will result in an error
sentence2[0] ="Our Majesty" # this will replace the zeroth index value with "Our Majesty"
# sentence1[30] = "!" # this returns error because str cannot be modified
sentence2[0:2] = ["we","want"] # this replaces the first two indexes with "We", "Want"
print(sentence2)