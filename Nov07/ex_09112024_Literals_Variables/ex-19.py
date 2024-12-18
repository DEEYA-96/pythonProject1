name = 'Python is both compiled and interpreted language'
print(type(name))
# name = name + 1 # cannot concatenate str and integer
name = name + str(1)  # (+) act has string concatenation by converting int into string
print(name)

fname = 'Deeya'
lname = 'HK'
FullName = fname + " " + lname
print(FullName)
