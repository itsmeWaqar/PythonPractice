def fibonacci(n):
    # Write your code here.
    if n in mem:
        return mem[n]
    if n<=1:
        return n
    else:
        v = fibonacci(n-1) + fibonacci(n-2)
        mem[n] = v
        return v
        
n = int(raw_input())
mem = {}
print(fibonacci(n))