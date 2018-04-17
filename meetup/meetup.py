import calendar
from datetime import date, timedelta

def meetup_day(year, month, day_of_the_week, which):
    def parse_day(initial):
        try:
            out_date = date(year, month, initial)
        except ValueError as a:
            print("Got one")
            raise MeetupDayException("Bad date buddy")

        while True:
            if out_date.strftime("%A") == day_of_the_week:
                return out_date
            else:
                out_date += timedelta(days = 1)


    if which == "1st":
        return parse_day(1)
    elif which == "2nd":
        return parse_day(8)
    elif which == "3rd":
        return parse_day(15)
    elif which == "4th":
        return parse_day(22)
    elif which == "5th":
        return parse_day(29)
    elif which == "teenth":
        return parse_day(13)
    elif which == "last":
        return parse_day(calendar.monthrange(year, month)[1] - 6)
    
class MeetupDayException(Exception):
    def __init__(self, message):
        super().__init__(message)

print(meetup_day(2015, 2, 'Monday', '5th'))