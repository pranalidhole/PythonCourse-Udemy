#range() function :
#upper limit is not included in range function
#lower limit is always included
#range function has one / two / three parameters as arguments
print("range function with one argument::")
a = range(5)
for i in a:
    print(i)
print("range function with two arguments:")
b = range(1,10)
for i in b:
    print(i)
print("range function with 3 arguments:")
c = range(2,10,2)
for i in c:
    print(i)

#set() - collection of elements without any duplicate values
#sets are unordered, no sequence
#eg - {'apple','orange','mango'}
#set treats every character of the string as a separate element
q = set('abc')
print(q) #{'c','b','a'}
w = set('abcaa')
print(w) #{'c', 'a', 'b'} #no duplicated
r = set(['apple','orange','banana'])
print(r)
#LOOPS:
#for and while loop
for i in range(-2,3):
    print(i)
name = 'pranali'
print("looping strings:")
for value in name:
    print(value)

#while loop:
print("while loop example:")
i = 0
while(i<5):
    print(i)
    i=i+1




