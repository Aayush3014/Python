def up(s):
   
    return s.upper()

s = "welcome to python class"
l = list(map(up,s))
a = ''.join(l)
print(a)