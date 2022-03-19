# Strings: text and binary data

s = 'Hello World!'
type(s)
# upper() and lower() change case of string as in the name
s.upper() 
s.lower()
# strip() takes trailing and leading chars out of string, if parameter not specified,
# will default to whitespace
s.strip('!')
s[0] # Python uses 0th indexing, so this will return 'H'
s[6:] # ':' can be used to specify range of characters. this will return 6th char -> end,
# or "World!"
s[6:-1] # returns 'World', since -1 means to access second char from the END
len(s)
b=s.encode()
b
type(b)
c=b.decode()
c
type(c)
t = ' This is a simple program.'
s + t
print('"{:s}" has {:d} characters.' .format(s,len(s)))
