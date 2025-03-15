a = (1,45,342,3424,False, 45, "Rohan", "Shivam")
print(a) 

print(len(a))

t1 = a.count(45) # Returns number of times 45 occurs in a.
print(t1)

t2 = a.index(45) # Returns the index of first occurrence of 45 in a.
print(t2)

t3 = a*2 # Tuples can be repeated using the '*' operator
print(t3)

print(342 in a) # Check if an element exists in tuple
print(341 in a)

t4 = a[2:5] # Slicing of tuples, slicing of a tuples gives a new tuple
print(t4)