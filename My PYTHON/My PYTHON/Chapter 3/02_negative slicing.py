# name = "J|a|r|v|i|s" --> Length = 6
#         0|1|2|3|4|5  --> [0:6]
#        -6-5-4-3-2-1  --> [-6,-1]

name = "jarvis"
print(name[0:6])

print(name[-6: -2])
print(name[0:4])

print(name[:3]) # is same as print(name[0:4]) , here the empty space before colon represents 0
print(name[1:]) # is same as print(name[1:6]) , here the empty space after colon represents "length"

# Skip value
word = "amazing"
word[1: 7: 2] # "mzn"
# step 1 - ressolve [1:7] = mazing
# step 2 - select first letter = 'm'
# step 3 - select letter at 2nd place choosing from the letter after m = 'z'
# step 4 - continue the process untill the word ends 