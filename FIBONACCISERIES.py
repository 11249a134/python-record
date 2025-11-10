//Aim:To write a Python program that generates the Fibonacci sequence up to N terms, where N > 0. The program should display an error message if the entered value of N is not greater than zero.
//Algorithm:
1.Start the program.
2.Accept a value N from the user.
3.Check if N > 0:
4.If not, display an error message and stop the program.
5.Define a function fibonacci(N) to generate the Fibonacci sequence.
6.Inside the function:
7.Initialize the first two numbers as 0 and 1.
8.Use a loop to generate the next terms using the formula:
9.Fn = Fn-1 + Fn-2.
10.Print the sequence up to N terms.
11.Call the function with the user-provided value.
12.Stop the program.
//Program:
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
//Result: A program that generates the Fibonacci sequence up to N terms, where N > 0 is executed succesfully
