def get_fraction():
    while True:
        try:
            frac_str = input("Fraction: ").strip()
            x_str, y_str = frac_str.split("/")
            x = int(x_str)
            y = int(y_str)

            if x > y:
                continue

            return x, y

        except (ValueError, ZeroDivisionError):
             pass

def main():
    x, y = get_fraction()
    fraction = x / y
    percentage = round(fraction * 100)

    if percentage > 90:
        print("F")
    elif percentage < 10:
        print("E")
    else:
        print(f"{percentage}%")

if __name__ == "__main__":
    main()
