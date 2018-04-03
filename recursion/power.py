def power1(x,n):
    """
    Compute the value of x**n for the integer n
    """
    if n == 0:
        return 1
    else:
        return x*power(x,n-1)


def power(x,n):
    """Compute the value x**n for the integer n."""
    if n==0:
        return 1
    else:
        partial = power(x, n//2)  #rely on truncated division and is even
        result = partial*partial
        if n%2 ==1:  #if n odd, include extra factor of x
            result *=x
        return result

print(power(2,10000))
