def fibonacci_recursive_series(n):
    series = []
    def fib_recursive(num):
        if num <= 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fib_recursive(num - 1) + fib_recursive(num - 2)
    for i in range(n + 1):
        series.append(fib_recursive(i))
    print(f"Recursive Fibonacci Series up to {n}:")
    print(series)

def fibonacci_iterative_series(n):
    series = []
    if n >= 0:
        series.append(0)
    if n >= 1:
        series.append(1)
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        series.append(b)
    print(f"Iterative Fibonacci Series up to {n}:")
    print(series)


# Menu-driven program
def menu():
    while True:
        print("\n=== Fibonacci Calculator ===")
        print("1. Recursive Fibonacci Series")
        print("2. Iterative Fibonacci Series")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            n = int(input("Enter the value of n: "))
            fibonacci_recursive_series(n)
        elif choice == '2':
            n = int(input("Enter the value of n: "))
            fibonacci_iterative_series(n)
        elif choice == '3':
            print("Exiting program...")
            sys.exit()
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


# Run the menu
menu()
