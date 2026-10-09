from datetime import datetime

# Enter date of birth in YYYY-MM-DD format
birth_date = input("Enter your date of birth (YYYY-MM-DD): ")

try:
    dob = datetime.strptime(birth_date, "%Y-%m-%d").date()
    today = datetime.today().date()

    if dob > today:
        print("Date of birth cannot be in the future.")
    else:
        days_lived = (today - dob).days
        print(f"You have lived for {days_lived} days.")

except ValueError:
    print("Invalid date format! Please use YYYY-MM-DD.")
