"""
Clock Hands

Write a program which will take two inputs, a startTime and the endTime,
and calculates how many times the clock hands overlap in the given time
period.
"""


def check_overlap(position, hour):
    """Check overlap in first and last hours"""
    hour_clock_position = position[0] + position[1] / 60
    minute_clock_position = position[1] / 5
    overlap = 0
    if position[0] > 12:
        hour_clock_position = position[0] - 12
    if hour == 'first hour':
        # overlap = 1 if minut clock behind hour clock.
        overlap = hour_clock_position // minute_clock_position
    if hour == 'last hour':
        # overlap = 1 if hour clock behind minut clock.
        overlap = minute_clock_position // hour_clock_position
    return overlap


def count_full_hours_in_period(start, end):
    """
    Count full hours between start and end, ex: 23:59-1:10 = 1 full hour.
    """
    full_hours_period = 0
    if end[0] < start[0]:
        full_hours_period = end[0] + 24 - (start[0] + 1)
    else:
        full_hours_period = end[0] - (start[0] + 1)
    return full_hours_period


if __name__ == '__main__':
    TIME_PERIOD = input("Input time period (13:30-21:20): ").split('-')
    START_TIME = list(map(int, TIME_PERIOD[0].split(':')))
    END_TIME = list(map(int, TIME_PERIOD[1].split(':')))
    RESULT = (check_overlap(START_TIME, 'first hour') +
              count_full_hours_in_period(START_TIME, END_TIME) +
              check_overlap(END_TIME, 'last hour'))
    print("The clock hands overlap {} times in the given time period.\
          ".format(int(RESULT)))
