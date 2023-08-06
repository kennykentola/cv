year = 1900


if not year % 400:
    is_leap_year = True
elif not year % 100:
    is_leap_year = False
elif not year % 4:
    is_leap_year = True
else:
    is_leap_year

s_ly = ' is a ' if is_leap_year else 'is not a '
print('{:4d} {:s} leap year' .format(year, s_ly))

