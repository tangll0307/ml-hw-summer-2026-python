N = int(input("Enter N (positive integer): "))

numbers = []
for i in range(N):
    num = int(input(f"Enter number #{i + 1}: "))
    numbers.append(num)

X = int(input("Enter X: "))

if X in numbers:
    index = numbers.index(X) + 1  # convert to 1-based index
    print(index)
else:
    print(-1)
