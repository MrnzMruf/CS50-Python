def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    length = len(s)

    # Check max and min length     # Check just digit and char     # Check 2 first charachter
    if 2 <= length <=6 and s.isalnum() and s[0:2].isalpha():
        for c in s:
            if c.isdigit():
                index = s.index(c)
                if s[index:].isdigit() and c != '0':
                    return True
                else:
                    return False

        return True

main()
