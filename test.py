def fib(n):    # Serie de Fibonacci
     "Serie de Fibonacci hasta %s" % n
     a, b = 0, 1
     while b < n:
        print b,
        a, b = b, a+b

