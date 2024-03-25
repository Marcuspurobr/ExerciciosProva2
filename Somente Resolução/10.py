def Fibonacci(n):
    if n==1 or n==2:
        return 1
    if n%2==0:
        return 2*Fibonacci((n//2)+1)*Fibonacci(n//2)-Fibonacci(n//2)**2
    return (Fibonacci((n//2)+1))**2+(Fibonacci(n//2))**2
for d in range(1,20):
    print(Fibonacci(d))