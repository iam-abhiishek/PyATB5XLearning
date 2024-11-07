#print("Hello World")
#print("Abhishek Kumar")

#print(self, *args, sep=' ', end='\n', file=None): # known special case of print

# *args - unlimited number of comma separated arguments
#      print("abc",123,"hello")  IndentationError: unexpected indent

print("abc",123,"hello")
print("abc",123,"hello",sep='-',end='  ')
print("abc",123,"hello",sep='-')
