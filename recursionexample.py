# #Factorial: 5! =5*4*3*2*1
# #Recursion 
# import sys 
# print(sys.getrecursionlimit())

#fibonacci Sequence 
def fibonacci(n):
    if n == 1:
        return 1 
    elif n == 2:
        return 1 
    elif n>2:
        return fibonacci(n-1) + fibonacci(n-2)
        
