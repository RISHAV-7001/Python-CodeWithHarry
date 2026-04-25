s = "hello world"   #strings are immutable

#s[0] = "R"         #you cannot do this

a = len(s)
print(a)
print(s.upper())            #output : "HELLO WORLD"
print(s.lower())            #output : "hello world"
print(s.capitalize())       #output : "Hello world"
print(s.title())            #output : "Hello World"