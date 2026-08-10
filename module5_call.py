from module5_mod import NumberStorage


def main():
    storage = NumberStorage()

    n = int(input("Enter N (positive integer): "))

    for i in range(n):
        num = int(input(f"Enter number #{i + 1}: "))
        storage.insert(num)

    x = int(input("Enter X: "))
    print(storage.search(x))


if __name__ == "__main__":
    main()
