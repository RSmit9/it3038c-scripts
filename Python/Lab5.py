print ("Lets see how many seconds old you are!")
print ("How old are you? Enter your birth day, month, and year as a number when prompted")
year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))

YearAge = 2023 - year



YearSeconds = YearAge * 31536000
MonthSeconds = month * 2628288
DaySeconds = day * 86400

age = YearSeconds + MonthSeconds + DaySeconds
print ("You are " , age , " old and counting!")
