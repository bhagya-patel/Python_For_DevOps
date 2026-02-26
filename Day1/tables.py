choice = input("Enter the choice (press q to Quit): ")

while choice != "q":
    num = int(input("Enter the number you want the table for: "))

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    choice = input("Enter the choice (press q to Quit): ")
