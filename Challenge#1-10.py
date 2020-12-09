#1
def multiples_sum(x):
    '''
    (int)->int
    >>> multiples_sum(10)
    23
    >>> multiples_sum(1000)
    233168
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000

    >>> 
    '''
    multiple=[]
    for i in range(x):
        if i%3==0 or i%5==0:
            multiple.append(i)
    return sum(multiple)
            
        
#2

def Fibonacci(limit):
    x=0
    y=1
    total=0
    while y <= limit:
        tmp=y
        y=x+y
        x=tmp   # x,y=y,x+y
        if y%2==0:
            total+=y
            
    print( total)
    
