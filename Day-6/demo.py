def is_leap_year(year):
    if year%400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


def print_calender(n, year):
    feb_num_day = 29 if is_leap_year(year) else 28
    month_dict = {
        1: 31,
        2: feb_num_day,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    for i in range(1, n + 1):
        print("Month:", i)
        for j in range(1, month_dict.get(i) + 1):
            print(j, end=" ")
        print()


if __name__ == '__main__':
    year = 2000
    print_calender(2, year)
    # import calendar
    # # initializing the year and month
    # year = 2020
    # month = 1
    # # printing the calendar
    # print(calendar.month(year, month))
