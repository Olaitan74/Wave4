# Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is. For example, calling the function and printing the result like this:

# print(readable_timedelta(10))

# should output the following:

# 1 week(s) and 3 day(s).


# write your function here
def readable_timedelta(days):
    week = days // 7
    day = days % 7
    if week > 1 and day > 1:
        return "{} weeks and {} days".format(week, day)
    elif week > 1 and day <= 1:
        return "{} weeks and {} day".format(week, day)
    elif week == 1 and day > 1:
        return "{} week and {} days".format(week, day)
    elif week == 1 and day <= 1:
        return "{} week and {} day".format(week, day)
    else:
        return "Input too low or not recognized"


# test your function
print(readable_timedelta(10))
