import re

# Define a regular expression pattern to match datetime strings
datetime_pattern = r'^((?:19|20)\d\d)-(0?[1-9]|1[0-2])-(0?[1-9]|[12]\d|3[01]) (0?\d|1\d|2[0-3]):(0?\d|[1-5]\d):(0?\d|[1-5]\d)$'


# use regular expression to check if user's ddl is valid
def validate_deadline(user_deadline):
    return bool(re.match(pattern=datetime_pattern, string=user_deadline))
