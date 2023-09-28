import datetime

# # Getting Current Date and Time
# now = datetime.datetime.now()
# print(f"Current Date and Time: {now}")

# # Creating a Specific Date
# date = datetime.date(2023, 9, 24)  # year, month, day
# print(f"Specific Date: {date} och {type(date)}")


# # Creating a Specific Time
# time = datetime.time(12, 30, 45)  # hour, minute, second
# print(f"Specific Time: {time}")

# # Formatting Date and Time
# now = datetime.datetime.now()
# # formatted_date = now.strftime("%A-->%B %d %Y %H:%M:%S")
# formatted_date = now.strftime("Dag i veckan:%A månad:%B")
# print(f"Formatted Date and Time: {formatted_date}")

# # Calculating the Difference Between Two Dates
# date1 = datetime.date(2023, 11, 23)
# date2 = datetime.date(2023, 10, 24)

# date_difference = date2 - date1
# print(f"Difference between {date2} and {date1} is: {date_difference.days} days")

# Adding or Subtracting Time from a Date
now = datetime.datetime.now()
one_week_later = now + datetime.timedelta(weeks=1,days=2, hours=3)

print(f"Now: {now}")
print(f"One week later: {one_week_later}")

# # Parsing Date String
# date_string = "2023-09-24 18:30:00"
# parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
# print(f"Parsed Date and Time: {parsed_date}")

# # Convert datetime to timestamp
# date_string = "2023-09-24 18:30:00"
# parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
# print(f"Parsed Date and Time: {parsed_date}")


