import calendar

year = 2021
month = 9

print(calendar.month(year, month))

# Printing calendar as HTML
new_cal = calendar.HTMLCalendar(firstweekday = 0)

print(new_cal.formatmonth(2021, 8, withyear = True))

# Check the leap year
x = calendar.leapdays(2016, 2020)
y = calendar.isleap(2002)
z = calendar.isleap(2005)

print(x)
print(y)
print(z)

# Getting the full calendar
year = 2021
print(calendar.calendar(year))