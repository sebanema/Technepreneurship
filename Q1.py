def Fibonacci():
    n = 100
#The first two numbers in the sequence
    n1, n2 = 0, 1
#The nth term of the sequence
    nterm = 0
#var. nterm is printed as new number following implementation of Fib.
    while nterm < n:
        print(n1)
        seq = n1 + n2
        n1 = n2
        n2 = seq
        nterm += 1
Fibonacci()
