def add_time(start_time, duration, start_day=None):
    start_time_sp = start_time.split()[0]
    am_pm = start_time.split()[1]
    hour = int(start_time_sp.split(":")[0])
    minute = int(start_time_sp.split(":")[1])
    dur_hour = int(duration.split(":")[0])
    dur_minute = int(duration.split(":")[1])
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    n = 0
    end_day = ""
    end_hour = 0
    end_minute = minute + dur_minute
    if end_minute >= 60:
        end_minute = end_minute - 60
        hour = hour + 1

    if dur_hour >= 24:
        d = int(dur_hour / 24)
        n = n + d
        dur_hour = dur_hour - 24 * n

    if am_pm == "AM" and hour < 12:
        end_hour = hour + dur_hour
        if end_hour > 12:
            end_hour = end_hour - 12
            am_pm = "PM"
            if end_hour > 12:
                end_hour = end_hour - 12
                am_pm = "AM"
                n = n + 1
        elif end_hour == 12:
            am_pm = "PM"
    elif am_pm == "AM" and hour == 12:
        end_hour = hour + dur_hour - 12
        if end_hour > 12:
            end_hour = end_hour - 12
            am_pm = "PM"
        elif end_hour == 12:
            am_pm = "PM"
        elif end_hour == 0:
            end_hour = 12
    elif am_pm == "AM" and hour > 12:
        end_hour = hour + dur_hour - 12
        if 12 < end_hour < 24:
            end_hour = end_hour - 12
            am_pm = "PM"
            if end_hour > 12:
                end_hour = end_hour - 12
        elif end_hour >= 24:
            end_hour = end_hour - 12
            n = n + 1
            if end_hour > 12:
                end_hour = end_hour - 12
    elif am_pm == "PM":
        end_hour = hour + dur_hour
        if 12 < end_hour <= 24:
            end_hour = end_hour - 12
            am_pm = "AM"
            n = n + 1
        elif end_hour == 12:
            am_pm = "AM"
            n = n + 1

    str_end_hour = str(end_hour)
    str_end_minute = ""
    if end_minute < 10:
        str_end_minute = "0" + str(end_minute)
    elif end_minute >= 10:
        str_end_minute = str(end_minute)

    if start_day is None:
        if n == 0:
            print(str_end_hour + ":" + str_end_minute, am_pm)
        elif n == 1:
            print(str_end_hour + ":" + str_end_minute, am_pm + " (next day)")
        elif n > 1:
            print(str_end_hour + ":" + str_end_minute, am_pm + " (" + str(n) + " days later)")
    elif start_day.lower() in days:
        m = days.index(start_day.lower())
        m = m + n % 7
        if m > 6:
            m = m - 7
        end_day = days[m].capitalize()
        if n == 0:
            print(str_end_hour + ":" + str_end_minute, am_pm + ", " + end_day)
        elif n == 1:
            print(str_end_hour + ":" + str_end_minute, am_pm + ", " + end_day + " (next day)")
        elif n > 1:
            print(str_end_hour + ":" + str_end_minute, am_pm + ", " + end_day + " (" + str(n) + " days later)")
