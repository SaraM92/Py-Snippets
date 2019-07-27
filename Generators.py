#WWCodePython
# Python Generators 
# A generator for Fibonacci Numbers 
def fib(top):     
  # Initialize first two Fibonacci Numbers  
  a, b = 0, 1
  # yield next Fibonacci Number 
  while a < top: 
    yield a 
    a, b = b, a + b 
# Create a generator object 
x = fib(5) 
#Using multiple prints to display the next number in the #series
print(x.__next__())
print(x.__next__())
print(x.__next__())
#using a loop to disply the series
for i in fib(5):
  print(i)
