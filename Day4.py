# Print function
print('Hello Pushparghya')

# String
message = 'Hello Suparna'
print(message)

# When to use string in ('') or (" ") or (''' ''')
# String with single quote
message2 = "Sankha's world"
print(message2)

# string with double quotes
message3 = 'Never go to "Behala" this year'
print(message3)

# multi line statements
message4 = '''
Hi Pushparghya,

Trust you are doing well!
'''
print(message4)

# find the length of a string
name = 'Hello Pushparghya'
print("Length :", len(name))

# index starts from 0
# get char by index,
print("Index at 10 :", name[10])
print("get the whole string :", name[0:len(name)])

# get only Hello, it will start from 0 to 4(5-1)
print("name[0:5] :", name[0:5])

# get only Pushparghya, it will take from 6th index till the end
print("name[6:] :", name[6:])

# Extended slicing
print("Print char w/o 1 :", name[0::1])

# -ve direction
word = "python"
print(word[-1], word[-2], word[-3])
print(word[:2] + word[2:])