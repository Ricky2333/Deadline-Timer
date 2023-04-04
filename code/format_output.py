# padding
padding = 25
width = 90

# format the output
def print_f(text, status):
    # define the text to display
    # calculate the width of the output
    # width = len(text) + 2 * padding

    # print the message with formatting
    if status == "begin":   # print upper "====="
        print("=" * width)

    print(f"{' ' * padding}{text}{' ' * padding}".center(width))  # print text

    if status == "end": # print lower "===="
        print("=" * width)
