import datetime, bday_messages


today = datetime.date.today()

next_birthday = datetime.date(year = 2026, month=7, day= 12)

time_difference = next_birthday - today

days_away = time_difference.days

print(days_away)


if next_birthday == today:
    print(bday_messages.message)
else:
    print(f'My next birthday is {days_away} days away!')