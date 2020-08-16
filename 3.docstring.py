def readable_timedelta(days):
    # insert your docstring here
    """Calculate the number of week(s) and day(s).
    INPUT:
    days: this is the total number of days and it is an int.
    OUTPUT:
    week(s) and day(s): (days // 7) which is the number of week(s) and (days % 7) will be the number of day(s)
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
