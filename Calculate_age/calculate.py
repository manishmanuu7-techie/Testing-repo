from datetime import date


# Get date of birth from the user
print("=== Age Calculator ===")

day = int(input("Enter the day you were born (1-31): "))
month = int(input("Enter the month you were born (1-12): "))
year = int(input("Enter the year you were born: "))


# Create the birth date
try:
    birth_date = date(year, month, day)
except ValueError:
    print("Invalid date. Please enter a valid date.")
    exit()


# Get today's date
today = date.today()


# Check if the birth date is in the future
if birth_date > today:
    print("Your date of birth cannot be in the future.")
    exit()


# Calculate age in years
age_years = today.year - birth_date.year

# If the birthday hasn't happened yet this year, subtract one year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age_years -= 1


# Calculate remaining months and days
last_birthday = date(
    birth_date.year + age_years,
    birth_date.month,
    birth_date.day
)

# Calculate months
if today.month >= last_birthday.month:
    age_months = today.month - last_birthday.month
else:
    age_months = 12 + today.month - last_birthday.month


# Calculate days
if today.day >= last_birthday.day:
    age_days = today.day - last_birthday.day
else:
    age_months -= 1

    # Find the number of days in the previous month
    if today.month == 1:
        previous_month = 12
        previous_year = today.year - 1
    else:
        previous_month = today.month - 1
        previous_year = today.year

    days_in_previous_month = (
        date(today.year, today.month, 1)
        - date(previous_year, previous_month, 1)
    ).days

    age_days = days_in_previous_month - last_birthday.day + today.day


# Calculate total days alive
total_days = (today - birth_date).days


# Display the results
print("\n=== Your Age ===")
print("Date of birth:", birth_date.strftime("%d-%m-%Y"))
print("Today's date:", today.strftime("%d-%m-%Y"))

print(
    "Your age is:",
    age_years,
    "years,",
    age_months,
    "months, and",
    age_days,
    "days."
)

print("You have been alive for", total_days, "days.")
