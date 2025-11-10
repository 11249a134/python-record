def fibonacci(N):
    a, b = 0, 1
    print("Fibonacci sequence:")
    for i in range(N):
        print(a, end=" ")
        a, b = b, a + b
N = int(input("Enter the number of terms (N > 0): "))
if N <= 0:
    print("Error: Please enter a value greater than 0.")
else:
    fibonacci(N)