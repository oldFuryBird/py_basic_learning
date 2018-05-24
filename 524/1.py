# sequence 
# list and tuple, string  Unicode string buffer obj xtrange
# list 
edward = ['edward Gumby',42]

john = ['john Smith',50]

database = [edward, john]

print(database)

# sequence common action  indexing,sliceing,adding,multiplying,has,length,max,min
# iteration 

# indexing
greeting = "Hello"
print(greeting[0]) # H

# sliceing

tag = '<a href="http://www.python.org">Python web site </a>'

print(tag[9:30]) #http://www.python.org include 9 except 30 index  sliceing [start,end)

# if start < end : the sliced sequence is empty   

print(tag[-20:]) # Python web site </a> -20 to the last

print(tag[:8]) # <a href=

# step 
numbers = list(range(0,10))
print(numbers[0:10:2])
print(numbers[0:10:3])
print(numbers[10:0:-1]) # resort

# adding 
print([1,2,3] + [4,5,6])

# multiply
print([1,2,3] * 2)
print('Hello ' * 5)

# has 
print('H' in 'Hello')
print(1 in [1,2,3])
print([1,2] in [1,2,3]) # False

# lenght ,min , max
num = [ 100 ,34, 678]
print(len(num),max(num),min(num))

s = "Hello world"
print(len(s),max(s),min(s)) # 11 w  
