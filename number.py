# Take input as int and return output as string

def main():

    x = inputvalue()

    if x == 0:
        return("0")

    # Checking for negative values
    if x < 0:
        negative = True
        x = x * (-1)
    else:
        negative = False

    # Create empty list
    output = []

    while x > 0:

        # Get last digit
        y = x % 10

        # Using ASCII table where 0 = 48
        z = chr(y + 48)

        # Moving to next digit
        x //= 10

        output.append(z)

    output.reverse()

    # Merge elements in list to one string and print the output as a string
    output = "".join(output)

    # Adding "-" if negative input
    if negative:
        return("-" + output)
    else:
        return(output)


# Prompt user for input of type int
def inputvalue():
    while True:
        try:
            n = int(input("Please insert an integer: "))
        except ValueError:
            print("Error: The value is not an integer.")
            continue
        else:
            break
    return n


main()