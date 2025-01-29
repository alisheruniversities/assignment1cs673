def print_multiplication_table():
    for i in range(1, 13):
        for j in range(1, 13):
            print(f"{i * j:4}", end=" ")
        print()

print_multiplication_table()