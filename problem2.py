def fib(n):
        result = []
        a, b = 0,1
        while b < n:
            if b % 2 == 0:
                result.append(b)
            a, b = b, a+b
        return sum(result)

