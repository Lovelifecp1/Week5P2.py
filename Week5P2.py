def bookstore_points():
    print("CSU Global Bookstore Points Calculator")
    print("--------------------------------------")

    while True:
        try:
            books_purchased = int(input("Enter the number of books purchased this month: "))
            if books_purchased < 0:
                print("The number of books cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if books_purchased == 0:
        points = 0
    elif books_purchased == 2:
        points = 5
    elif books_purchased == 4:
        points = 15
    elif books_purchased == 6:
        points = 30
    elif books_purchased >= 8:
        points = 60

    print(f"\nBooks Purchased: {books_purchased}")
    print(f"Points Earned: {points}")


bookstore_points()
