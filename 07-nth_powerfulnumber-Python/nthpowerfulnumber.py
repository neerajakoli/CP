# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def nthpowerfulnumber(x): 
    if(x==0):
        return 1
    c=0
    n=4
    powerful = n
    while(c<x):
        if(isPowerful(n)):
            c+=1
            powerful=n
        n+=1
    return powerful

def isPowerful(n):
    if(isPrime(n)):
        return False
    for i in range(2,int(n/2+1)):
        if((n%i)==0):
            if(isPrime(i)):
                if not(n%(i*i)==0):
                    return False

    return True

def isPrime(n):    
    if(n<2):
        return False
    if(n==2):
        return True
    for i in range(2,int((n/2)+1)):
        if (n%i==0):
            return False
    return True 