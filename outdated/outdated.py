def get_date():
    months = [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
    ]

    while True:
        date_input = input("Enter a date (month-day-year or Month day, year): ").strip()

        # Check if the input is in "month-day-year" format (e.g., 9/8/1636)
        if "/" in date_input:
            try:
                month, day, year = map(int, date_input.split("/"))
                if 1 <= month <= 12 and 1 <= day <= 31:  # Validate month and day ranges
                    # Format the date as YYYY-MM-DD
                    formatted_date = f"{year:04}-{month:02}-{day:02}"
                    print(formatted_date)
                    break
            except ValueError:
                pass  # If conversion fails, continue the loop

        # Check if the input is in "Month day, year" format (e.g., September 8, 1636)
        elif "," in date_input:  # Check if there's a comma (for Month day, year format)
            try:
                # Remove any extra spaces and handle the format "Month day, year"
                parts = date_input.split()
                month_name = parts[0]
                day = int(parts[1].replace(",", ""))  # Remove comma from day
                year = int(parts[2])

                month = months.index(month_name) + 1  # Get month number
                if 1 <= month <= 12 and 1 <= day <= 31:  # Validate month and day ranges
                    # Format the date as YYYY-MM-DD
                    formatted_date = f"{year:04}-{month:02}-{day:02}"
                    print(formatted_date)
                    break
            except (ValueError, IndexError):
                pass  # If there are any errors, continue the loop

        print("Invalid date format. Please try again.")

get_date()
