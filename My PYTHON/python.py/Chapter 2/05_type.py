a = "31.2"
t = type(a) # class <int>
print(t)
b = float(a) # a but the type of a should be float
print(b)
q = type(b)
print(q)


str(31) == "31" # integer to string conversion
int("32") == 32 # string to integer conversion 
float(32) == 32.0 # integer to float conversion