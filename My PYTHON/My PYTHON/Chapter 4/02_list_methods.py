friends = ['Apple','orange',7,302.07,False] # Lists can store any and multiple set of values
print(friends)

friends.append('Jarvis') # Inserts value at the end of list
print(friends) # (Lists are mutable)

l1 = [1, 34, 62, 2, 6, 11]
l1.sort() # Sorts/ arranges list in ascending order
print(l1)

l2 = [1, 34, 62, 2, 6, 11]
l2.reverse() # Reverses the set of values in the list
print(l2)

l3 = [1, 34, 62, 2, 6, 11]
l3.insert(2, 333333) # Insert 333333 such that its index in the list is 2
print(l3)

l4 = [1, 34, 62, 2, 6, 11]
l4.pop(3) # Delete element at index 3
print(l4)
l5 = [1, 34, 62, 2, 6, 11]
value = l5.pop(3) # Returns the element at index 3 
print(value)

l6 = [1, 34, 62, 2, 6, 11]
l6.remove(62) # Removes the given element from list , doesn't removes a part of any element from list 
print(l6) 
