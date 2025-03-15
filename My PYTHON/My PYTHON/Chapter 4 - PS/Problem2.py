marks = []

m1 = int(input("Enter marks here: ")) # Now due to 'int' function string made by 'input' function is changed into an integer
marks.append(m1)
m2 = int(input("Enter marks here: "))
marks.append(m2)
m3 = int(input("Enter marks here: "))
marks.append(m3)
m4 = int(input("Enter marks here: "))
marks.append(m4)
m5 = int(input("Enter marks here: "))
marks.append(m5)
m6 = int(input("Enter marks here: "))
marks.append(m6)

marks.sort() # Sorts the marks(integers) into ascending order

print(marks)