def average_rainfall():
    print("Average Rainfall Calculator")
    print("---------------------------")

    while True:
        try:
            years = int(input("Enter the number of years: "))
            if years < 1:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    total_rainfall = 0
    total_months = years * 12

    for year in range(1, years + 1):
        print(f"\nYear {year}:")
        for month in range(1, 13):
            while True:
                try:
                    rainfall = float(input(f"  Enter rainfall (in inches) for month {month}: "))
                    if rainfall < 0:
                        print("Rainfall cannot be negative. Please try again.")
                    else:
                        total_rainfall += rainfall
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")

    average_rainfall = total_rainfall / total_months

    print("\nRainfall Summary:")
    print(f"Total months: {total_months}")
    print(f"Total rainfall: {total_rainfall:.2f} inches")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")


average_rainfall()

