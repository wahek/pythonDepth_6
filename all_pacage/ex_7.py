import calendar

__all__ = ['is_leap']


def is_leap(year: int):
    return calendar.isleap(year)
