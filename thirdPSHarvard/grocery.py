def main():
    groceries = {}

    while True:
        try:
            item = input().strip().lower()

            if item:
                groceries[item] = groceries.get(item, 0) + 1

        except EOFError:
            break

    for item in sorted(groceries):
        print(groceries[item], item.upper())


main()