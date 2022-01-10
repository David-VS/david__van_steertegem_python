class Time:
    h: int = 0
    m: int = 0
    s: int = 0

    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self) -> str:
        return str(self.h)+":"+str(self.m)+":"+str(self.s)


class TimeUtils:

    def __init__(self):
        pass

    @staticmethod
    def add_time(time1, time2) -> Time:
        hours = 0
        minutes = 0
        seconds = 0

        seconds = time1.s + time2.s
        if seconds >= 60:
            seconds -= 60
            minutes += 1

        minutes += (time1.m + time2.m)
        if minutes >= 60:
            minutes -= 60
            hours += 1

        hours += (time1.h + time2.h)

        return Time(hours, minutes, seconds)

    @staticmethod
    def time_to_seconds(time) -> int:
        return time.s + (time.m * 60) + (time.h * 3600)
