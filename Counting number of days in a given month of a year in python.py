import calendar
def days_in_month(year, month):
    return calendar.monthrange(year, month)[1]
year = 2024
month = 2  # February
print(f"Number of days: {days_in_month(year, month)}")
