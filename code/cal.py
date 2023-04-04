from datetime import datetime


# calculate the difference
def calculate(user_dict):
    # get the current time
    time_now = datetime.now()

    # parse user input into a datetime object
    time_ddl = datetime.strptime(user_dict['ddl'], "%Y-%m-%d %H:%M:%S")

    if time_ddl < time_now:
        output = "\nDeadline already passed\n"
    else:
        # calculate the difference and return 'timedelta' object
        delta = (time_ddl - time_now)

        # parse
        delta_days = delta.days
        delta_hours = delta.seconds // 3600
        delta_minutes = delta.seconds % 3600 // 60
        delta_seconds = delta.seconds % 60

        # construct the output
        output = "\n"
        if delta_days > 0:
            output += f"{delta_days} days "
        if delta_hours > 0:
            output += f"{delta_hours} hours "
        if delta_minutes > 0:
            output += f"{delta_minutes} minutes "
        if delta_seconds > 0:
            output += f"{delta_seconds} seconds"
        output += " to finish this event!\n"

    return output
