
#challenge1
def multiples_sum(x):
    '''
    (int)-->int
    '''
    total_sum=0
    for i in range(x):
        if i%3==0 or i%5==0:
            total_sum=total_sum+i
    return total_sum

#challenge2
def Fibonacci(f):
    '''
    (int)-->int
    '''
    x=0
    y=1
    total=0
    while y<f:
        tmp=y
        y=x+y
        x=tmp
        if y%2==0:
            total = total+y

    return total

#challenge3
def largest_prime_factor(x):
    '''
    (int)-->int
    '''
    i=1
    factor=1
    while i<=x:
        if x%i==0 and i!=1:
            x=x//i
            print(i)
            if i>factor:
                factor=i
        else:
            i+=1

    return factor

#challenge4
def largest_palindrome_product():
    '''
    (none)-->int'''
    largest=None
    for i in range(100,1000):
        for j in range(100,1000):
            x=i*j
            if is_palindrome(x):
                if largest==None or x>largest:
                    largest=x
    return largest
            
def is_palindrome(x):
    y=str(x)
    z=str(x)[::-1]
    if y==z:
        return True
    else:
        return False


#challenge5
def is_multiple(x,rangeenter):
    for i in range(2,rangeenter):
        if x%i!=0:
            return False
    return True


def smallest_multiple(n):
    while not is_multiple(n,21):
        n+=20
    return n


#challenge6
def sum_of_squares1(x):
    square_sum=0
    sum_square=0
    for i in range(1,x+1):
        square_sum=square_sum+i**2
    for j in range(1,x+1):
        sum_square=sum_square+j
        
    print((sum_square)**2)
    print(square_sum)

def sum_of_square2(x):
    #pattern of square of sum (x+1)*(x/2)  --> n*(n+1)/2
    #pattern of sum of square [(x* (x+1)) *(x+(x+1)) ]/6
    sum_square=((x+1)*(x/2))
    square_sum= (((x*(x+1))*(x+(x+1)))/6)
    print( (sum_square)**2)
    print(square_sum)
    print((sum_square)**2 -square_sum)
        
        
        
                
            
                
            
    
 
