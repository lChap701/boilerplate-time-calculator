from datetime import datetime, timedelta
days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
        4: "Friday", 5: "Saturday", 6: "Sunday"}


def add_time(start, duration, day=""):
    """
    Adds the duration time to the start time

    Args:
        start (str):     Represents the time to start on.
        duration (str):  Represents the amount of time to add.

    Returns:
        str: Returns the time after the duration
    """
    # Gets the time
    startTime = datetime.strptime(start, "%I:%M %p")

    # Based on:
    # https://www.reddit.com/r/FreeCodeCamp/comments/j9el2q/i_did_the_python_time_calculator_challenge_in_30/
    if day:
        day = day.title()

        # Uses the correct day based on the weekday
        while days[startTime.weekday()] != day:
            startTime += timedelta(1)   # Moves up 1 day

    # Gets the time after the set duration of time has passed
    finalTime = startTime + \
        timedelta(hours=float(duration.split(":")[
                  0]), minutes=float(duration[-2:]))

    # Gets the final day based on:
    # https://www.reddit.com/r/FreeCodeCamp/comments/j9el2q/i_did_the_python_time_calculator_challenge_in_30/
    if day:
        day = ", " + finalTime.strftime("%A")

    # Gets the day message based on:
    # https://www.reddit.com/r/FreeCodeCamp/comments/j9el2q/i_did_the_python_time_calculator_challenge_in_30/
    leftOver = finalTime.day - startTime.day

    if leftOver == 1:
        day += " (next day)"
    elif leftOver > 1:
        day += " (" + str(leftOver) + " days later)"

    return finalTime.time().strftime("%#I:%M %p") + day
