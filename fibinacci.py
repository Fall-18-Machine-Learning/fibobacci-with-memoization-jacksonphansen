fib1 = -1
fib2 = -1

def Fib(n):
    if (n <= 1):
        return n
    if(fibstruct[n-1]!=-1):
        fib1 = fibstruct[n-1]
    else:
        fib1 = Fib(n-1)
    if(fibstruct[n-2]!=-1):
        fib2 = fibstruct[n-2]
    else:
        fib2 = Fib(n-2)
    return fib1 + fib2
    
fibinacci = int(input('Find the nth fibinacci! \n N equals: '));
fibstruct = []
for i in range(fibinacci):
    fibstruct.append(-1)
print(Fib(fibinacci))
    

