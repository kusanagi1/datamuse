import datetime
from datetime import date


age_str = input("Enter your date of birth: ")
age_fromisoformat = datetime.datetime.fromisoformat(age_str)
age_date = age_fromisoformat.date()
age_in_days = date.today() - age_date
age = age_in_days.days

print("You're {age} days old!".format(age=age))

age_in_seconds = age_in_days.days * 60 * 60 * 24
print("You're {age_in_seconds} seconds old!".format(age_in_seconds=age_in_seconds))
