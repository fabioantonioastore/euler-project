WEEK = 7
THIRTY_DAYS = 30 * 4
THIRTY_ONE_DAYS = 31 * 7
YEAR = 1900
FIRST_YEAR_DAY = 2


def is_leap_year(year: int) -> int:
    if (year % 4 == 0) and (not (year % 100 == 0)):
        return True
    elif year % 400 == 0:
        return True
    return False


def get_february_days(year: int) -> int:
    if is_leap_year(year):
        return 29
    return 28


def get_first_day(year: int) -> int:
    if not year > YEAR:
        raise f"year must be greater than {YEAR}"

    actual_day = FIRST_YEAR_DAY
    total_years = year - YEAR

    for y in range(total_years):
        if is_leap_year(YEAR + y):
            if actual_day == 7:
                actual_day = 2
                continue
            if actual_day == 6:
                actual_day = 1
                continue
            actual_day += 2
            continue
        if actual_day == 7:
            actual_day = 1
            continue
        actual_day += 1

    return actual_day


def get_total_days(day: int, first_year: int, last_year: int) -> int:
    total_years = last_year - first_year + 1
    first_day = get_first_day(first_year)
    days_count = 0

    actual_day = first_day
    for y in range(total_years):
        for m in range(1, 13):
            if m == 2:
                total_days = get_february_days(first_year + y)
            elif m == 4 or m == 6 or m == 9 or m == 11:
                total_days = 30
            else:
                total_days = 31
            for i in range(total_days):
                if actual_day == day and i == 0:
                    days_count += 1
                if actual_day == 7:
                    actual_day = 1
                    continue
                actual_day += 1

    return days_count


print(get_total_days(1, 1901, 2000))
